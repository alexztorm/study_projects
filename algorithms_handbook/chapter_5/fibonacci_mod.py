from algorithms_handbook.chapter_5.fibonacci import fibonacci


def fibonacci_mod(n: int, m: int) -> int:
    period = pisano_period(m)
    n = n % period
    num = fibonacci(n)

    return num % m


def pisano_period(m: int) -> int:
    curr, next = 0, 1
    period = 0

    while True:
        tmp = next
        next = (curr + next) % m
        curr = tmp
        period = period + 1
        if curr == 0 and next == 1:
            return period
