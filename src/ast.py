from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union


# ---------------- Base ----------------

@dataclass(frozen=True)
class Span:
    line: int
    col: int


class ASTNode:
    span: Optional[Span]

    def to_dict(self) -> Dict[str, Any]:
        raise NotImplementedError


# ---------------- Program / Robot ----------------

@dataclass(frozen=True)
class Program(ASTNode):
    robot: "RobotDecl"
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Program", "robot": self.robot.to_dict()}


@dataclass(frozen=True)
class RobotDecl(ASTNode):
    name: str
    sensors: List["SensorDecl"] = field(default_factory=list)
    actuators: List["ActuatorDecl"] = field(default_factory=list)
    vars: List["VarDecl"] = field(default_factory=list)
    behaviors: List["BehaviorDecl"] = field(default_factory=list)
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "RobotDecl",
            "name": self.name,
            "sensors": [s.to_dict() for s in self.sensors],
            "actuators": [a.to_dict() for a in self.actuators],
            "vars": [v.to_dict() for v in self.vars],
            "behaviors": [b.to_dict() for b in self.behaviors],
        }


@dataclass(frozen=True)
class SensorDecl(ASTNode):
    name: str
    data_type: str
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "SensorDecl", "name": self.name, "dataType": self.data_type}


@dataclass(frozen=True)
class ActuatorDecl(ASTNode):
    name: str
    kind: str
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "ActuatorDecl", "name": self.name, "kind": self.kind}


@dataclass(frozen=True)
class VarDecl(ASTNode):
    name: str
    data_type: str
    init: Optional["Expr"] = None
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"type": "VarDecl", "name": self.name, "dataType": self.data_type}
        if self.init is not None:
            d["init"] = self.init.to_dict()
        return d


# ---------------- Behavior / State ----------------

@dataclass(frozen=True)
class BehaviorDecl(ASTNode):
    name: str
    initial_state: str
    states: List["StateDecl"]
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "BehaviorDecl",
            "name": self.name,
            "initialState": self.initial_state,
            "states": [s.to_dict() for s in self.states],
        }


@dataclass(frozen=True)
class StateDecl(ASTNode):
    name: str
    enter_on: Optional["Block"] = None
    update_on: Optional["Block"] = None
    exit_on: Optional["Block"] = None
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        d: Dict[str, Any] = {"type": "StateDecl", "name": self.name}
        if self.enter_on is not None:
            d["enter_on"] = self.enter_on.to_dict()
        if self.update_on is not None:
            d["update_on"] = self.update_on.to_dict()
        if self.exit_on is not None:
            d["exit_on"] = self.exit_on.to_dict()
        return d


# ---------------- Statements ----------------

class Stmt(ASTNode):
    pass


@dataclass(frozen=True)
class Block(ASTNode):
    statements: List[Stmt] = field(default_factory=list)
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Block", "statements": [s.to_dict() for s in self.statements]}


@dataclass(frozen=True)
class TransitionStmt(Stmt):
    cond: "Expr"
    target_state: str
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "TransitionStmt", "cond": self.cond.to_dict(), "target": self.target_state}


@dataclass(frozen=True)
class AssignStmt(Stmt):
    name: str
    value: "Expr"
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "AssignStmt", "name": self.name, "value": self.value.to_dict()}


@dataclass(frozen=True)
class ActionStmt(Stmt):
    actuator: str
    method: str
    args: List["Expr"] = field(default_factory=list)
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "type": "ActionStmt",
            "actuator": self.actuator,
            "method": self.method,
            "args": [a.to_dict() for a in self.args],
        }


# ---------------- Expressions ----------------

class Expr(ASTNode):
    pass


@dataclass(frozen=True)
class LiteralExpr(Expr):
    value: Any
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Literal", "value": self.value}


@dataclass(frozen=True)
class IdExpr(Expr):
    name: str
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Id", "name": self.name}


@dataclass(frozen=True)
class UnaryExpr(Expr):
    op: str
    right: Expr
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Unary", "op": self.op, "right": self.right.to_dict()}


@dataclass(frozen=True)
class BinaryExpr(Expr):
    left: Expr
    op: str
    right: Expr
    span: Optional[Span] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"type": "Binary", "left": self.left.to_dict(), "op": self.op, "right": self.right.to_dict()}
