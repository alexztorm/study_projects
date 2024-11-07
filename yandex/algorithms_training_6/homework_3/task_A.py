def right_bracket_seq(line: str) -> str:
    right_brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []

    if not line.strip():
        return 'yes'

    for bracket in line:
        if bracket in right_brackets.keys():
            stack.append(bracket)
        elif not stack:
            return 'no'
        elif right_brackets[stack[-1]] != bracket:
            return 'no'
        else:
            stack.pop()

    if not stack:
        return 'yes'
    else:
        return 'no'


brackets = input()

print(right_bracket_seq(brackets))

# print(right_bracket_seq('()[]'))
# print(right_bracket_seq('([)]'))
# print(right_bracket_seq('('))
# print(right_bracket_seq(']'))
# print(right_bracket_seq(''))
# print(right_bracket_seq(' '))
# print(right_bracket_seq('{()[]({})}[[])]'))
