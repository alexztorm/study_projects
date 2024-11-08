def calc_expr_2(expression: str):
    stack = []

    new_line = to_postfix_notation(expression)

    if new_line == 'WRONG':
        return new_line

    for i in range(len(new_line)):
        if type(new_line[i]) == int:
            stack.append(int(new_line[i]))
        else:
            if len(stack) < 2:
                return 'WRONG'
            num1 = stack.pop()
            num2 = stack.pop()
            if new_line[i] == '-':
                stack.append(num2 - num1)
            elif new_line[i] == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    if len(stack) > 1:
        return 'WRONG'
    else:
        return stack[0]


def to_postfix_notation(expression: str):
    res = []
    valid_symbols = '1234567890()+-* '
    stack = []

    if expression[0] in '+*':
        return 'WRONG'
    elif expression[0] == '-':
        expression = '0' + expression

    i = 0
    while i < len(expression):
        if expression[i] not in valid_symbols:
            return 'WRONG'
        if expression[i] == '(' and i+1 < len(expression) and expression[i+1] == '-':
            expression = expression[:i+1] + '0' + expression[i+1:]
        i += 1

    prev_num = False
    for i in range(len(expression)):
        # print(stack, res)
        if expression[i].isdigit():
            if prev_num:
                res[-1] = res[-1] * 10 + int(expression[i])
            else:
                res.append(int(expression[i]))
                prev_num = True
        elif expression[i] == '*':
            while stack and stack[-1] == '*':
                res.append(stack.pop())
            stack.append(expression[i])
            prev_num = False
        elif expression[i] in '+-':
            while stack and stack[-1] in '*+-':
                res.append(stack.pop())
            stack.append(expression[i])
            prev_num = False
        elif expression[i] == '(':
            stack.append(expression[i])
            prev_num = False
        elif expression[i] == ')':
            while stack and stack[-1] != '(':
                res.append(stack.pop())
            if stack:
                stack.pop()
            else:
                return 'WRONG'
            prev_num = False
        else:
            prev_num = False

    while stack:
        res.append(stack.pop())

    return res


# expr = input()
#
# print(calc_expr_2(expr))

print(calc_expr_2('1+(2*2 - 3)'))
print(calc_expr_2('1+a+1'))
print(calc_expr_2('1 1 + 2'))
print(calc_expr_2('-6+15-3*(-2-3)+1-5*(1-0)'))
print(calc_expr_2('*15-3*(-2-3)+1-5*(1-0)'))
print(calc_expr_2('(()))('))
print(calc_expr_2('1 + 2 + 3 + * - *'))
print(calc_expr_2('(1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))'))
print(calc_expr_2('1+((((((((((((2)-3)+4*6)-4)*4+4))))))))'))

print(eval('(1+(7+8)-(3-4*5)*(2*4)+(9)-(16728)*(123*9+2)+((2)))+((((((0-19283))))))'))
