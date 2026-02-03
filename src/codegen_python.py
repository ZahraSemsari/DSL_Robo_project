from __future__ import annotations

from typing import Any, Dict, List, Optional

from src.ast import (
    Program, RobotDecl, BehaviorDecl, StateDecl, Block,
    VarDecl,
    Stmt, TransitionStmt, AssignStmt, ActionStmt,
    Expr, LiteralExpr, IdExpr, UnaryExpr, BinaryExpr
)


def _py(s: str) -> str:
    return repr(s)

def _safe_ident(name: str) -> str:
    out = []
    for ch in name:
        out.append(ch if (ch.isalnum() or ch == "_") else "_")
    s = "".join(out) or "state"
    if s[0].isdigit():
        s = "_" + s
    return s


def emit_expr(e: Expr) -> str:
    if isinstance(e, LiteralExpr):
        return repr(e.value)
    if isinstance(e, IdExpr):
        return f"get_value({_py(e.name)})"
    if isinstance(e, UnaryExpr):
        if e.op in ("!", "not"):
            return f"(not {emit_expr(e.right)})"
        if e.op in ("+", "-"):
            return f"({e.op}{emit_expr(e.right)})"
        return f"({e.op}{emit_expr(e.right)})"
    if isinstance(e, BinaryExpr):
        op = e.op
        if op in ("&&", "and"):
            op = "and"
        elif op in ("||", "or"):
            op = "or"
        return f"({emit_expr(e.left)} {op} {emit_expr(e.right)})"
    raise TypeError(f"Unknown Expr: {type(e)}")


def emit_block(block: Optional[Block], indent: str) -> List[str]:
    if block is None or not block.statements:
        return [f"{indent}return None"]

    lines: List[str] = []
    for st in block.statements:
        if isinstance(st, AssignStmt):
            lines.append(f"{indent}vars[{_py(st.name)}] = {emit_expr(st.value)}")
        # vars['target'] = (get_value('target') + 1)

        elif isinstance(st, ActionStmt):
            args = ", ".join(emit_expr(a) for a in st.args)
            lines.append(f"{indent}actuators[{_py(st.actuator)}].{st.method}({args})")
        # actuators['heater'].on()

        elif isinstance(st, TransitionStmt):
            cond = emit_expr(st.cond)
            lines.append(f"{indent}if {cond}:")
            lines.append(f"{indent}    return {_py(st.target_state)}")

        # if (get_value('temperature') < get_value('target')):
        #     return 'Heating'

        else:
            raise TypeError(f"Unknown Stmt: {type(st)}")

    lines.append(f"{indent}return None")
    return lines


def generate_python(program: Program, behavior_name: Optional[str] = None) -> str:
    robot: RobotDecl = program.robot
    if not robot.behaviors:
        raise ValueError("No behaviors in robot.")

    behavior: BehaviorDecl
    if behavior_name is None:
        behavior = robot.behaviors[0]
    else:
        found = [b for b in robot.behaviors if b.name == behavior_name]
        if not found:
            raise ValueError(f"Behavior not found: {behavior_name}")
        behavior = found[0]

    states: Dict[str, StateDecl] = {s.name: s for s in behavior.states}

    out: List[str] = []
    out += [
        "# Auto-generated Python from RobotDSL",
        "from __future__ import annotations",
        "from dataclasses import dataclass",
        "from typing import Any, Dict, Optional, Callable",
        "",
        "class ActuatorBase:",
        "    def __init__(self, name: str):",
        "        self.name = name",
        "    def __getattr__(self, method: str):",
        "        def _f(*args, **kwargs):",
        "            print(f'[ACT] {self.name}.{method} args={args} kwargs={kwargs}')",
        "        return _f",
        "",
        "@dataclass",
        "class Ctx:",
        "    vars: Dict[str, Any]",
        "    sensors: Dict[str, Any]",
        "    actuators: Dict[str, Any]",
        "",
        "def get_value_factory(ctx: Ctx):",
        "    def get_value(name: str) -> Any:",
        "        if name in ctx.vars:",
        "            return ctx.vars[name]",
        "        return ctx.sensors.get(name, None)",
        "    return get_value",
        "",
        f"INITIAL_STATE = {_py(behavior.initial_state)}",
        "",
        "def make_vars() -> Dict[str, Any]:",
        "    vars: Dict[str, Any] = {}",
    ]

    for v in robot.vars:
        if v.init is None:
            out.append(f"    vars[{_py(v.name)}] = None")
        else:
            out.append(f"    vars[{_py(v.name)}] = None  # init in run()")
    out += [
        "    return vars",
        "",
        "def make_actuators() -> Dict[str, Any]:",
        "    a: Dict[str, Any] = {}",
    ]
    for a in robot.actuators:
        out.append(f"    a[{_py(a.name)}] = ActuatorBase({_py(a.name)})")
    out += [
        "    return a",
        "",
        "# -------- Handlers --------",
    ]

    # handlers
    for st_name, st in states.items():
        sid = _safe_ident(st_name)

        out += [f"def enter_{sid}(ctx: Ctx) -> None:"]
        out += ["    vars = ctx.vars", "    actuators = ctx.actuators", "    get_value = get_value_factory(ctx)"]
        out += emit_block(st.enter_on, indent="    ")
        out += [""]

        out += [f"def update_{sid}(ctx: Ctx) -> Optional[str]:"]
        out += ["    vars = ctx.vars", "    actuators = ctx.actuators", "    get_value = get_value_factory(ctx)"]
        out += emit_block(st.update_on, indent="    ")
        out += [""]

        out += [f"def exit_{sid}(ctx: Ctx) -> None:"]
        out += ["    vars = ctx.vars", "    actuators = ctx.actuators", "    get_value = get_value_factory(ctx)"]
        out += emit_block(st.exit_on, indent="    ")
        out += [""]

    # def update_Idle(ctx):
    #     vars = ctx.vars
    #     actuators = ctx.actuators
    #     get_value = get_value_factory(ctx)
    #
    #     if (get_value('temperature') < get_value('target')):
    #         return 'Heating'
    #     return None

    out += [
        "ENTER: Dict[str, Callable[[Ctx], None]] = {",
    ]
    for st_name in states.keys():
        out.append(f"    {_py(st_name)}: enter_{_safe_ident(st_name)},")
    out += ["}", "", "UPDATE: Dict[str, Callable[[Ctx], Optional[str]]] = {"]
    for st_name in states.keys():
        out.append(f"    {_py(st_name)}: update_{_safe_ident(st_name)},")
    out += ["}", "", "EXIT: Dict[str, Callable[[Ctx], None]] = {"]
    for st_name in states.keys():
        out.append(f"    {_py(st_name)}: exit_{_safe_ident(st_name)},")
    out += [
        "}",
        "",
        "class FSM:",
        "    def __init__(self, ctx: Ctx):",
        "        self.ctx = ctx",
        "        self.state = INITIAL_STATE",
        "        self._entered = False",
        "",
        "    def tick(self) -> None:",
        "        if not self._entered:",
        "            ENTER.get(self.state, lambda _c: None)(self.ctx)",
        "            self._entered = True",
        "        nxt = UPDATE.get(self.state, lambda _c: None)(self.ctx)",
        "        if nxt is not None and nxt != self.state:",
        "            EXIT.get(self.state, lambda _c: None)(self.ctx)",
        "            self.state = nxt",
        "            ENTER.get(self.state, lambda _c: None)(self.ctx)",
        "",
        "def run_demo(steps: int = 20):",
        "    ctx = Ctx(vars=make_vars(), sensors={}, actuators=make_actuators())",
        "    get_value = get_value_factory(ctx)",
        "    # init vars using DSL init expressions (if any):",
    ]

    for v in robot.vars:
        if v.init is not None:
            out.append(f"    ctx.vars[{_py(v.name)}] = {emit_expr(v.init)}")
    out += [
        "    fsm = FSM(ctx)",
        "    for i in range(steps):",
        "        print(f'[TICK {i}] state={fsm.state} vars={ctx.vars} sensors={ctx.sensors}')",
        "        # update sensors here if needed",
        "        fsm.tick()",
        "    print('[DONE]', 'state=', fsm.state, 'vars=', ctx.vars)",
        "",
        "if __name__ == '__main__':",
        "    run_demo()",
    ]

    return "\n".join(out)
