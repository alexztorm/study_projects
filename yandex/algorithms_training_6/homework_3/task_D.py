def calc_expr(expression: list[str]) -> int:
    stack = []

    for i in range(len(expression)):
        if expression[i].isdigit():
            stack.append(int(expression[i]))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if expression[i] == '-':
                stack.append(num2 - num1)
            elif expression[i] == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    return stack[0]


expr = input().split()

print(calc_expr(expr))

# print(calc_expr('8 9 + 1 7 - *'.split()))
# print(calc_expr('6 3 1 4 5 * + * 2 * +             '.split()))
