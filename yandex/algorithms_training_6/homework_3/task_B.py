def laylandia(n: int, costs: list[int]) -> list[int]:
    res = [-1] * n
    stack = []

    for i in range(len(costs)):
        if not stack:
            stack.append((i, costs[i]))
        else:
            while stack and stack[-1][1] > costs[i]:
                mod = stack.pop()
                res[mod[0]] = i
            stack.append((i, costs[i]))

    return res


m = int(input())
nums = [int(x) for x in input().split()]

ans = laylandia(m, nums)

for item in ans:
    print(item, end=' ')
