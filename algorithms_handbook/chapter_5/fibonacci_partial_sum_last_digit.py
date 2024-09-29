from algorithms_handbook.chapter_5.fibonacci_sum_last_digit import fibonacci_sum_last_digit


def fibonacci_partial_sum_last_digit(m: int, n: int) -> int:
    sum_less_m = fibonacci_sum_last_digit(m - 1)
    sum_more_m = fibonacci_sum_last_digit(n)

    if sum_more_m < sum_less_m:
        return sum_more_m + 10 - sum_less_m
    else:
        return sum_more_m - sum_less_m


a, b = map(int, input().split())

print(fibonacci_partial_sum_last_digit(a, b))
