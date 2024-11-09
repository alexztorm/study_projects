def min_psp(n: int, w: str, s: str) -> str:
    res = ''
    stack = []
    expected_len = 0

    for bracket in s:
        if bracket in '([':
            stack.append(bracket)
            res += bracket
            expected_len += 2
        else:
            stack.pop()
            res += bracket

    priorities = {'(': 0, ')': 0, '[': 0, ']': 0}

    for i in range(len(w)):
        priorities[w[i]] = i

    while stack or len(res) < n:
        if not stack:
            if expected_len == n:
                break
            else:
                if priorities['('] < priorities['[']:
                    stack.append('(')
                    res += '('
                    expected_len += 2
                else:
                    stack.append('[')
                    res += '['
                    expected_len += 2
        else:
            if expected_len == n:
                if stack[-1] == '(':
                    stack.pop()
                    res += ')'
                else:
                    stack.pop()
                    res += ']'
            else:
                if stack[-1] == '(':
                    max_priority = min(priorities['('], priorities['['], priorities[')'])
                    if max_priority == priorities['(']:
                        stack.append('(')
                        res += '('
                        expected_len += 2
                    elif max_priority == priorities['[']:
                        stack.append('[')
                        res += '['
                        expected_len += 2
                    else:
                        stack.pop()
                        res += ')'
                else:
                    max_priority = min(priorities['('], priorities['['], priorities[']'])
                    if max_priority == priorities['(']:
                        stack.append('(')
                        res += '('
                        expected_len += 2
                    elif max_priority == priorities['[']:
                        stack.append('[')
                        res += '['
                        expected_len += 2
                    else:
                        stack.pop()
                        res += ']'

    return res


m = int(input())
a = input()
b = input()

print(min_psp(m, a, b))

# print(min_psp(6, '()[]', '([('))
# print(min_psp(6, '][)(', '(['))
# print(min_psp(4, '(][)', '()[]'))
# print(min_psp(4, '([])', ''))
