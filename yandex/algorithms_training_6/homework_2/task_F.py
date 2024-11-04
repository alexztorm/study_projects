def sum_of_multiplications_3(n: int, numbers: list[int]) -> int:
    if n == 3:
        return (numbers[0] * numbers[1] * numbers[2]) % 1000000007
    else:
        mult_sum = 0

        pref_sum = [0]

        for i in range(n):
            pref_sum.append(pref_sum[i] + numbers[i])

        for i in range(1, n - 1):
            mult_sum += calc_prefix_sum(0, i - 1, pref_sum) * numbers[i] * calc_prefix_sum(i + 1, n - 1, pref_sum)

        return mult_sum % 1000000007


def calc_prefix_sum(l: int, r: int, prefix_sum: list[int]) -> int:
    return prefix_sum[r + 1] - prefix_sum[l]


# m = int(input())
# nums = [int(x) for x in input().split()]

# print(sum_of_multiplications_3(m, nums))

print(sum_of_multiplications_3(3, [1, 2, 3]))
print(sum_of_multiplications_3(4, [0, 5, 6, 7]))
print(sum_of_multiplications_3(4, [10**6, 10**5 + 1, 10**5 + 3, 7]))
print(sum_of_multiplications_3(5, [10, 6, 10, 3, 7]))   # test 3
print(sum_of_multiplications_3(3, [143461, 574468, 902994]))   # test 7
