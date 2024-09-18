def evaluate_expression(expression, values):
    for key, value in values.items():
        expression = expression.replace(key, str(value))
    return eval(expression)

expression = "(A and B) or (not C)"
values = {'A': True, 'B': False, 'C': True}

result = evaluate_expression(expression, values)
print("The result of the expression is:", result)