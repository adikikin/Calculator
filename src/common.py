from enum import Enum, auto

class States_enum(Enum):
    START = auto()
    ERROR = auto()
    STORING_DIGITS_FOR_FIRST_OPERAND = auto()
    STORED_OPERAND = auto()
    STORED_OPERATOR = auto()
    STORING_DIGITS_FOR_SECOND_OPERAND = auto()

class Buttons_Enum(Enum):
    ADD = "+"
    SUB = "-"
    MUL = "x"
    DIV = "/"
    EQUAL = "="
    CLEAR = "C"
