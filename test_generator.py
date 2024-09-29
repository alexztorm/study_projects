from random import randint
from algorithms_handbook.chapter_5.fibonacci_sum_last_digit import fibonacci_sum_last_digit


def generate_test(n: int) -> list[int]:
    restriction = 10**5
    test = [randint(0, restriction) for i in range(n)]
    return test


def fibonacci_sum_last_digit_2(n: int) -> int:
    if n <= 1:
        return n
    else:
        old_prev = 0
        prev = 1
        last_sum = 1

        for i in range(n - 1):
            tmp = old_prev
            old_prev = prev
            prev += tmp
            prev = prev % 10
            last_sum += prev
            last_sum = last_sum % 10

        return last_sum


test1 = generate_test(100)

for el in test1:
    sum_a = fibonacci_sum_last_digit_2(el)
    sum_b = fibonacci_sum_last_digit(el)

    if sum_a != sum_b:
        print(el, sum_a, sum_b, "Not OK")
