
# DSL_Robo_project

## Robot DSL Compiler (ANTLR4 + Python)

This project implements a **Domain-Specific Language (DSL)** for defining and executing
robot behaviors using a **Finite State Machine (FSM)** model.

A DSL script is parsed with **ANTLR4**, converted into an **Abstract Syntax Tree (AST)**,
and then translated into **executable Python code**.

## Pipeline

DSL file  
↓  
ANTLR Parse Tree  
↓  
AST (Abstract Syntax Tree)  
↓  
Python Code Generation  
↓  
Executable Robot Controller (FSM)


The final output is a standalone Python program (`generated_robot.py`) that simulates
the robot behavior.

---

## What Is a “Robot” in This Project?

In this project, a robot is **not a physical robot**, but a **behavior controller**.

The robot:
- Reads inputs from **sensors**
- Maintains internal **variables**
- Controls **actuators**
- Switches between **states** based on conditions

The behavior is modeled as a **Finite State Machine**, which is a very common approach
in robotics and embedded systems.

---

## What Can This Robot Do?

Using this DSL, a robot can:

### 1) Read Sensors (Inputs)
Sensors represent data coming from the environment.

Example:
```dsl
sensor temperature: float;
sensor distance: float;
````

Typical use cases:

* Temperature sensors
* Distance / ultrasonic sensors
* Buttons
* Light sensors
* Battery level sensors

Sensors are **read-only** and are provided at runtime.

---

### 2) Store Internal State (Variables)

Variables represent the robot’s internal memory.

Example:

```dsl
var target: float = 30.0;
var speed: int = 100;
```

Variables:

* Can be initialized
* Can be updated during execution
* Are used in conditions and calculations

---

### 3) Control Actuators (Outputs)

Actuators represent things the robot can control.

Example:

```dsl
actuator heater: Heater;
actuator motor: Motor;
```

Inside behaviors:

```dsl
heater.on();
motor.setSpeed(100);
```

Typical actuators:

* Motors
* LEDs
* Heaters
* Servos
* Buzzers

In this project, actuators are **simulated** and print actions to the console,
but they can easily be connected to real hardware.

---

### 4) Define Behavior Using States

Robot behavior is defined using **states**.

Each state can have:

* `enter_on`  → runs once when entering the state
* `update_on` → runs every tick
* `exit_on`   → runs once when leaving the state

Example:

```dsl
state Heating {
  enter_on {
    heater.on();
  }
  update_on {
    if (temperature >= target) goto Idle;
  }
  exit_on {
    heater.off();
  }
}
```

---

### 5) Transition Between States

Transitions are defined using conditions:

```dsl
if (temperature < target) goto Heating;
```

This allows the robot to:

* React to sensor values
* Change behavior dynamically
* Implement decision logic

---

## Example Robot Behavior

A simple temperature controller:

* If temperature is below target → turn heater ON
* If temperature reaches target → turn heater OFF

This same DSL can be used for:

* Obstacle avoidance robots
* Line follower robots
* Automatic doors
* Traffic light controllers
* Smart home automation logic

---

## Project Structure

```
DSL_Robo_project/
  grammar/
    RobotDSL.g4              # ANTLR grammar
  src/
    generated/               # ANTLR-generated parser/lexer
    ast.py                   # AST node definitions
    ast_builder_listener.py  # Parse Tree → AST
    semantic.py              # Semantic analysis
    codegen_python.py        # Python code generation
    main.py                  # CLI entry point
  examples/
    TempBot.dsl              # Example DSL program
```

---

## Command-Line Usage

### Print AST

```bash
python -m src.main examples/TempBot.dsl ast
```

### Semantic Check

```bash
python -m src.main examples/TempBot.dsl check
```

### Generate Python Code

```bash
python -m src.main examples/TempBot.dsl genpy --out generated_robot.py
```

### Run Generated Code

```bash
python generated_robot.py
```

---

## Design Goals

* Clear separation between **syntax**, **semantics**, and **execution**
* Readable and simple DSL
* FSM-based behavior modeling
* Executable code generation instead of interpretation
* Easy extension for real robotics projects

---
