def window_min(n: int, k: int, numbers: list[int]) -> list[int]:
    if k <= 1:
        return numbers
    elif n == k:
        return [min(numbers)]

    res = []
    deque = []

    for i in range(n):
        if not deque:
            deque.append(numbers[i])
        else:
            while deque and deque[-1] > numbers[i]:
                deque.pop()
            deque.append(numbers[i])

            if i >= k - 1:
                res.append(deque[0])

                if deque[0] == numbers[i - k + 1]:
                    deque.pop(0)

    return res


a, b = map(int, input().split())
nums = [int(x) for x in input().split()]

ans = window_min(a, b, nums)

for item in ans:
    print(item)

# print(window_min(7, 3, [1, 3, 2, 4, 5, 3, 1]))
# print(window_min(7, 1, [1, 3, 2, 4, 5, 3, 1]))
# print(window_min(7, 7, [1, 3, 2, 4, 5, 3, 1]))
# print(window_min(13, 4, [7, 5, 3, 6, 2, 8, 1, 1, 5, 9, 4, 3, 5]))
