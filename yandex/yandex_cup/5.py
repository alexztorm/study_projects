def maya_combinations(target: int, magic_numbers: list[int]) -> int:
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(64):
        print(dp)
        weight = 2 ** i
        new_dp = dp[:]

        for num_gi in magic_numbers:
            if num_gi > 0:
                for j in range(target + 1):
                    if j >= weight * num_gi:
                        new_dp[j] = (new_dp[j] + dp[j - weight * num_gi]) % (10 ** 9 + 7)

        dp = new_dp

    return dp[n]


n = int(input())
m = int(input())
magic_nums = [int(x) for x in input().split()]

print(maya_combinations(n, magic_nums))
