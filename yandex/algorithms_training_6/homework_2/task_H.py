def move_to_openspace(n: int, numbers: list[int]) -> int:
    pref_sum = [0]
    post_sum = [0]

    for i in range(n):
        pref_sum.append(pref_sum[i] + numbers[i])

    for i in range(n - 1, -1, -1):
        post_sum.append(post_sum[n - i - 1] + numbers[i])

    pref_pref_sum = [0]
    pref_post_sum = [0]

    for i in range(1, n + 1):
        pref_pref_sum.append(pref_pref_sum[i - 1] + pref_sum[i])
        pref_post_sum.append(pref_post_sum[i - 1] + post_sum[i])

    min_ans = pref_pref_sum[0] + pref_post_sum[n - 1]

    for i in range(1, n):
        new_min = pref_pref_sum[i] + pref_post_sum[n - 1 - i]

        if new_min < min_ans:
            min_ans = new_min

    return min_ans


m = int(input())
nums = [int(x) for x in input().split()]

print(move_to_openspace(m, nums))

print(move_to_openspace(4, [5, 2, 3, 1]))
print(move_to_openspace(5, [5, 4, 3, 2, 1]))
