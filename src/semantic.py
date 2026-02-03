from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

from src.ast import (
    Program, RobotDecl, BehaviorDecl, StateDecl, Block,
    VarDecl, SensorDecl, ActuatorDecl,
    Stmt, TransitionStmt, AssignStmt, ActionStmt,
    Expr, LiteralExpr, IdExpr, UnaryExpr, BinaryExpr, Span
)

PRIM_TYPES = {"bool", "int", "float", "string"}


@dataclass(frozen=True)
class SemanticError:
    message: str
    span: Optional[Span] = None

    def __str__(self) -> str:
        if self.span:
            return f"[{self.span.line}:{self.span.col}] {self.message}"
        return self.message


class SemanticAnalyzer:
    def __init__(self, program: Program) -> None:
        self.program = program
        self.errors: List[SemanticError] = []

        self.sensors: Dict[str, str] = {}
        self.vars: Dict[str, str] = {}
        self.actuators: Dict[str, str] = {}

    def error(self, msg: str, span: Optional[Span]) -> None:
        self.errors.append(SemanticError(msg, span))

    def analyze(self) -> List[SemanticError]:
        r = self.program.robot

        self._collect_decls(r)
        for b in r.behaviors:
            self._check_behavior(b)

        return self.errors


    def _collect_decls(self, r: RobotDecl) -> None:
        # sensors
        for s in r.sensors:
            if s.name in self.sensors:
                self.error(f"Duplicate sensor: {s.name}", s.span)
            self.sensors[s.name] = s.data_type

        # actuators
        for a in r.actuators:
            if a.name in self.actuators:
                self.error(f"Duplicate actuator: {a.name}", a.span)
            self.actuators[a.name] = a.kind

        # vars
        for v in r.vars:
            if v.name in self.vars:
                self.error(f"Duplicate var: {v.name}", v.span)
            if v.name in self.sensors:
                self.error(f"Var name conflicts with sensor: {v.name}", v.span)
            if v.name in self.actuators:
                self.error(f"Var name conflicts with actuator: {v.name}", v.span)
            self.vars[v.name] = v.data_type

            if v.init is not None:
                t_init = self._infer_expr_type(v.init)
                if t_init is not None and not self._assignable(v.data_type, t_init):
                    self.error(
                        f"Cannot init var '{v.name}' of type {v.data_type} with {t_init}",
                        v.span
                    )



    def _check_behavior(self, b: BehaviorDecl) -> None:
        state_map: Dict[str, StateDecl] = {}
        for st in b.states:
            if st.name in state_map:
                self.error(f"Duplicate state '{st.name}' in behavior '{b.name}'", st.span)
            state_map[st.name] = st

        if b.initial_state not in state_map:
            self.error(
                f"Behavior '{b.name}' initial state '{b.initial_state}' not found",
                b.span
            )

        for st in b.states:
            for blk in (st.enter_on, st.update_on, st.exit_on):
                if blk:
                    self._check_block(blk, state_map)

    def _check_block(self, blk: Block, state_map: Dict[str, StateDecl]) -> None:
        for s in blk.statements:
            if isinstance(s, TransitionStmt):
                # cond type should be bool
                t = self._infer_expr_type(s.cond)
                if t is not None and t != "bool":
                    self.error(f"Transition condition must be bool, got {t}", s.span)

                if s.target_state not in state_map:
                    self.error(f"goto target state '{s.target_state}' not found", s.span)

            elif isinstance(s, AssignStmt):
                if s.name in self.sensors:
                    self.error(f"Cannot assign to sensor '{s.name}' (read-only)", s.span)
                if s.name in self.actuators:
                    self.error(f"Cannot assign to actuator '{s.name}'", s.span)
                if s.name not in self.vars:
                    self.error(f"Assign to undeclared var '{s.name}'", s.span)
                else:
                    rhs_t = self._infer_expr_type(s.value)
                    if rhs_t is not None and not self._assignable(self.vars[s.name], rhs_t):
                        self.error(
                            f"Type mismatch: cannot assign {rhs_t} to var '{s.name}' ({self.vars[s.name]})",
                            s.span
                        )

            elif isinstance(s, ActionStmt):
                if s.actuator not in self.actuators:
                    self.error(f"Unknown actuator '{s.actuator}'", s.span)
                # args types inferred (برای undefined ids هم خطا می‌دهد)
                for a in s.args:
                    self._infer_expr_type(a)
            else:
                self.error(f"Unknown statement node: {type(s)}", getattr(s, "span", None))


    def _infer_expr_type(self, e: Expr) -> Optional[str]:
        if isinstance(e, LiteralExpr):
            if isinstance(e.value, bool):
                return "bool"
            if isinstance(e.value, int):
                return "int"
            if isinstance(e.value, float):
                return "float"
            if isinstance(e.value, str):
                return "string"
            return None

        if isinstance(e, IdExpr):
            name = e.name
            if name in self.vars:
                return self.vars[name]
            if name in self.sensors:
                return self.sensors[name]
            self.error(f"Use of undeclared identifier '{name}'", e.span)
            return None

        if isinstance(e, UnaryExpr):
            rt = self._infer_expr_type(e.right)
            if rt is None:
                return None
            op = e.op
            if op in ("!", "not"):
                if rt != "bool":
                    self.error(f"Unary '{op}' expects bool, got {rt}", e.span)
                    return None
                return "bool"
            if op in ("+", "-"):
                if rt not in ("int", "float"):
                    self.error(f"Unary '{op}' expects number, got {rt}", e.span)
                    return None
                return rt
            self.error(f"Unknown unary operator '{op}'", e.span)
            return None

        if isinstance(e, BinaryExpr):
            lt = self._infer_expr_type(e.left)
            rt = self._infer_expr_type(e.right)
            if lt is None or rt is None:
                return None

            op = e.op
            if op in ("&&", "and", "||", "or"):
                if lt != "bool" or rt != "bool":
                    self.error(f"Logical '{op}' expects bool,bool got {lt},{rt}", e.span)
                    return None
                return "bool"

            if op in ("==", "!="):
                if lt == rt:
                    return "bool"
                if {lt, rt} <= {"int", "float"}:
                    return "bool"
                self.error(f"Equality '{op}' expects comparable types, got {lt},{rt}", e.span)
                return None

            if op in ("<", "<=", ">", ">="):
                if {lt, rt} <= {"int", "float"}:
                    return "bool"
                self.error(f"Comparison '{op}' expects numbers, got {lt},{rt}", e.span)
                return None

            if op in ("+", "-", "*", "/", "%"):
                if {lt, rt} <= {"int", "float"}:
                    # division promotes to float
                    if op == "/":
                        return "float"
                    return "float" if "float" in (lt, rt) else "int"
                if op == "+" and lt == rt == "string":
                    return "string"
                self.error(f"Arithmetic '{op}' expects numbers (or string+string), got {lt},{rt}", e.span)
                return None

            self.error(f"Unknown binary operator '{op}'", e.span)
            return None

        self.error(f"Unknown expression node: {type(e)}", getattr(e, "span", None))
        return None

    def _assignable(self, to_t: str, from_t: str) -> bool:
        if to_t == from_t:
            return True
        if to_t == "float" and from_t == "int":
            return True
        return False


def analyze(program: Program) -> List[SemanticError]:
    return SemanticAnalyzer(program).analyze()
