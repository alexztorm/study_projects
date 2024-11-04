def clues(n: int, a_list: list[int], m: int, k: int, x_list: list[int]) -> list[int]:
    res = []

    pref_sum = [0] * n

    for i in range(1, n):
        if a_list[i - 1] == a_list[i]:
            pref_sum[i] = pref_sum[i - 1] + 1
        else:
            pref_sum[i] = pref_sum[i - 1]

    # print(pref_sum)

    left, right = 0, 1
    steps = [1]
    while left < n:
        while right < n and calc_pref_sum(left, right, pref_sum) <= k:
            if a_list[right] >= a_list[right - 1]:
                steps.append(left + 1)
            else:
                left = right
                steps.append(right + 1)
            right += 1
        left += 1

    # print(steps)

    for item in x_list:
        res.append(steps[item - 1])

    return res


def calc_pref_sum(l: int, r: int, pref_sum: list[int]) -> int:
    return pref_sum[r] - pref_sum[l]


# n1 = int(input())
# a = [int(x) for x in input().split()]
# m1, k1 = map(int, input().split())
# x = [int(x) for x in input().split()]
#
# ans = clues(n1, a, m1, k1, x)
#
# for num in ans:
#     print(num, end=" ")

tests = [
    [6, [3, 3, 3, 4, 4, 5], 4, 2, [3, 4, 5, 6]],
    [7, [1, 5, 7, 2, 10, 10, 6], 7, 0, [1, 2, 3, 4, 5, 6, 7]],
    [9, [3, 2, 2, 3, 4, 2, 5, 5, 2], 1, 1, [8]],
    [17, [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9], 1, 2, [17]],
    [5, [4, 4, 4, 4, 4], 3, 1, [1, 3, 5]],
    [8, [1, 2, 2, 1, 3, 3, 2, 1], 5, 1, [2, 3, 5, 7, 8]],
    [1, [1], 1, 1, [1]]
]

answers = [
    [1, 1, 2, 2],
    [1, 1, 1, 4, 4, 6, 7],
    [6],
    [12],
    [1, 2, 4],
    [1, 1, 4, 7, 8],
    [1]
]

j = 0
for test in tests:
    new_ans = clues(test[0], test[1], test[2], test[3], test[4])
    if new_ans != answers[j]:
        print(f'program answer = {new_ans}, answer = {answers[j]}, test = {test}')
    else:
        print('OK')
    j += 1
