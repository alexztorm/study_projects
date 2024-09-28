def fibonacci_mod(n: int, m: int) -> int:
    period = pisano_period(m)
    n = n % period
    num = fibonacci(n)

    return num % m


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        old_prev = 0
        prev = 1

        for i in range(n - 1):
            tmp = old_prev
            old_prev = prev
            prev += tmp

        return prev


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


a, b = map(int, input().split())

print(fibonacci_mod(a, b))
