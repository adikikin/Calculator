# Calculator

Calculator is a desktop app that preforms arithmetic operations (multiplication, division, subtraction and addition) by the user's choice. 

## Design
Calculator is using MVC architecture. The Model component is implementing the state machine logic with State design pattern and State Factory.

### State Machine
The state changes, if needed, according to the user input as described in the figure:
![alt text](https://github.com/adikikin/Calculator/blob/Adi/design/state%20machine.jpg)

### Expression
The Expression tree is implemented using Composite design pattern and built after the raw expression is converted to postfix expression. 
Arithmetic operations are performed by correct precedence.

## Install
```bash
git clone https://github.com/adikikin/Calculator
```
## Run
```bash
python3 run.py
```
