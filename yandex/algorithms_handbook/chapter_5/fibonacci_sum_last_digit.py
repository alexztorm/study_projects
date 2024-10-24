from yandex.algorithms_handbook.chapter_5.fibonacci_mod import pisano_period


def fibonacci_sum_last_digit(n: int) -> int:
    period = pisano_period(10)
    n = n % period

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
