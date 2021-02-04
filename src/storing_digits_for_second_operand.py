from src.state import State
from src.states_enum import States_enum

class Storing_digits_for_second_operand(State):
    def __init__(self, i_state_factory, i_model, expression):
        State.i_factory = i_state_factory
        State.i_model = i_model
        State.expression = expression
        State.next_state_enum = None

    def add_digit(self, digit):
        return State.update_expression_and_model(self, 
                                                 State.expression.add_digit_to_second_operand, 
                                                 States_enum.STORING_DIGITS_FOR_SECOND_OPERAND,
                                                 digit)


    def add_operator(self, operator):
        result = self.__try_to_operate_expression(State.expression.add_operator, operator)
        if result != States_enum.ERROR.name:        
            State.next_state_enum = States_enum.STORED_OPERATOR
            State.update_model_with_next_state(self)
            return operator
        else:
            return result



    def evaluate(self):
        result = self.__try_to_operate_expression(State.expression.evaluate, None)
        if result != States_enum.ERROR.name:
            State.next_state_enum = States_enum.STORED_OPERAND
            State.update_model_with_next_state(self)
        return result


    def __try_to_operate_expression(self, expression_func, arg):
        try:
            if arg == None:
                return expression_func()
            else:
                return expression_func(arg)
        except ZeroDivisionError:
            State.update_expression_and_model(self, 
                                              State.expression.reset_expression, 
                                              States_enum.ERROR,
                                              None)
            return States_enum.ERROR.name




    def restart(self):
        return State.update_expression_and_model(self,
                                                 State.expression.reset_expression, 
                                                 States_enum.START,
                                                 None)
 