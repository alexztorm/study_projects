def sum_of_multiplications_3(n: int, numbers: list[int]) -> int:
    if n == 3:
        return (numbers[0] * numbers[1] * numbers[2]) % 1000000007
    else:
        mult_sum = 0
        right = 2

        while right < n:
            mult_sum += numbers[right - 2] * numbers[right - 1] * numbers[right]
            right += 1

        return mult_sum % 1000000007


# m = int(input())
# nums = [int(x) for x in input().split()]

# print(sum_of_multiplications_3(m, nums))

print(sum_of_multiplications_3(3, [1, 2, 3]))
print(sum_of_multiplications_3(4, [0, 5, 6, 7]))
print(sum_of_multiplications_3(4, [10**6, 10**5 + 1, 10**5 + 3, 7]))
print(sum_of_multiplications_3(5, [10, 6, 10, 3, 7]))
