"""Calculator.
The program expects the user to enter a mathematical expression
and displays the result. The calculator supports operations: addition,
subtraction, multiplication, division and addition to degree.
"""


def parse_expression(expression):
    """The function parses an expression, defines values and operators,
    and returns a list of tokens"""
    tokens = []
    for char in expression:
        if char.isdigit():
            tokens.append(float(char))
        elif char in "+-*/^":
            tokens.append(char)
    return tokens


def priority(op):
    """The function determines the priority of the operator"""
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0


def apply_operator(operators, values):
    """The function extracts the operator from the stack and
    the values to the left and right of the operator"""
    operand = operators.pop()
    right = values.pop()
    left = values.pop()
    if operand == '+':
        values.append(left + right)
    elif operand == '-':
        values.append(left - right)
    elif operand == '*':
        values.append(left * right)
    elif operand == '/':
        values.append(left / right)
    elif operand == '^':
        values.append(left ** right)


def evaluate_expression(tokens):
    """The function defines values and operators and does the calculation
    according to the priority of the operators"""
    values = []
    operators = []
    for token in tokens:
        if isinstance(token, float):
            values.append(token)
        else:
            while operators and priority(operators[-1]) >= priority(token):
                apply_operator(operators, values)
            operators.append(token)
    while operators:
        apply_operator(operators, values)
    return values[0]


def calculator():
    """Starting the program"""
    while True:
        expression = input("Enter a math expression "
                           "(or 'exit' to exit):").replace(' ', '')
        if expression.lower() == 'exit':
            return None

        try:
            tokens = parse_expression(expression)
            result = evaluate_expression(tokens)
            print(f"{result}")
        except ZeroDivisionError as e:
            print(e)
        except (IndexError, ValueError) as e:
            print(e)


calculator()
