def prefix_sum_k(n: int, k: int, numbers: list[int]) -> int:
    prefix_sum = [0]

    for i in range(n):
        prefix_sum.append(numbers[i] + prefix_sum[i])

    ans = 0
    r = 1
    for l in range(n + 1):
        while r < (n + 1):
            if prefix_sum[r] - prefix_sum[l] < k:
                r += 1
                continue
            elif prefix_sum[r] - prefix_sum[l] == k:
                ans += 1
                break
            else:
                break

    return ans


a, b = map(int, input().split())
nums = [int(x) for x in input().split()]

print(prefix_sum_k(a, b, nums))
