from operator import (add, sub, mul, truediv)

def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    supported = '+ - * /'.split()
    lhs, operator, rhs = calculation.split()
    try:
        if operator in supported:
            # casting should raise ValueError if not int
            operands = [int(operand) for operand in [lhs, rhs]]
            calc = {'+': add, '-': sub, '*': mul, '/': truediv}
            return calc.get(operator)(*operands)
        else:
            raise ValueError
    except ZeroDivisionError:
        raise ValueError
    
