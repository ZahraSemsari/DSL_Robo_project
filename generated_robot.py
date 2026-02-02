# Auto-generated Python from RobotDSL
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Optional, Callable

class ActuatorBase:
    def __init__(self, name: str):
        self.name = name
    def __getattr__(self, method: str):
        def _f(*args, **kwargs):
            print(f'[ACT] {self.name}.{method} args={args} kwargs={kwargs}')
        return _f

@dataclass
class Ctx:
    vars: Dict[str, Any]
    sensors: Dict[str, Any]
    actuators: Dict[str, Any]

def get_value_factory(ctx: Ctx):
    def get_value(name: str) -> Any:
        if name in ctx.vars:
            return ctx.vars[name]
        return ctx.sensors.get(name, None)
    return get_value

INITIAL_STATE = 'Idle'

def make_vars() -> Dict[str, Any]:
    vars: Dict[str, Any] = {}
    vars['target'] = None  # init in run()
    return vars

def make_actuators() -> Dict[str, Any]:
    a: Dict[str, Any] = {}
    a['heater'] = ActuatorBase('heater')
    return a

# -------- Handlers --------
def enter_Idle(ctx: Ctx) -> None:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    return None

def update_Idle(ctx: Ctx) -> Optional[str]:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    if (get_value('temperature') < get_value('target')):
        return 'Heating'
    return None

def exit_Idle(ctx: Ctx) -> None:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    return None

def enter_Heating(ctx: Ctx) -> None:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    actuators['heater'].on()
    return None

def update_Heating(ctx: Ctx) -> Optional[str]:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    if (get_value('temperature') >= get_value('target')):
        return 'Idle'
    return None

def exit_Heating(ctx: Ctx) -> None:
    vars = ctx.vars
    actuators = ctx.actuators
    get_value = get_value_factory(ctx)
    actuators['heater'].off()
    return None

ENTER: Dict[str, Callable[[Ctx], None]] = {
    'Idle': enter_Idle,
    'Heating': enter_Heating,
}

UPDATE: Dict[str, Callable[[Ctx], Optional[str]]] = {
    'Idle': update_Idle,
    'Heating': update_Heating,
}

EXIT: Dict[str, Callable[[Ctx], None]] = {
    'Idle': exit_Idle,
    'Heating': exit_Heating,
}

class FSM:
    def __init__(self, ctx: Ctx):
        self.ctx = ctx
        self.state = INITIAL_STATE
        self._entered = False

    def tick(self) -> None:
        if not self._entered:
            ENTER.get(self.state, lambda _c: None)(self.ctx)
            self._entered = True
        nxt = UPDATE.get(self.state, lambda _c: None)(self.ctx)
        if nxt is not None and nxt != self.state:
            EXIT.get(self.state, lambda _c: None)(self.ctx)
            self.state = nxt
            ENTER.get(self.state, lambda _c: None)(self.ctx)

def run_demo(steps: int = 20):
    ctx = Ctx(vars=make_vars(), sensors={}, actuators=make_actuators())
    ctx.sensors["temperature"] = 25.0
    get_value = get_value_factory(ctx)
    # init vars using DSL init expressions (if any):
    ctx.vars['target'] = 30.0
    fsm = FSM(ctx)
    for i in range(steps):
        ctx.sensors["temperature"] = 25.0 + i  # هر تیک یک درجه زیاد
        print(f'[TICK {i}] state={fsm.state} vars={ctx.vars} sensors={ctx.sensors}')
        # update sensors here if needed
        fsm.tick()
    print('[DONE]', 'state=', fsm.state, 'vars=', ctx.vars)

if __name__ == '__main__':
    run_demo()