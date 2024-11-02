def best_rest(n: int, k: int, numbers: list[int]) -> int:
    days = 1
    numbers.sort()

    left, right = 0, 1

    while left < n and right < n:
        if abs(numbers[left] - numbers[right]) <= k:
            days += 1
            right += 1
        else:
            left += 1
            right += 1

    return days


a, b = map(int, input().split())
nums = [int(x) for x in input().split()]

print(best_rest(a, b, nums))

print(best_rest(3, 2, [4, 2, 1]))
print(best_rest(9, 2, [3, 8, 5, 7, 1, 2, 4, 9, 6]))
print(best_rest(3, 0, [1, 3, 1]))
print(best_rest(4, 4, [32, 77, 1, 100]))
print(best_rest(3, 1, [106, 101, 106]))
