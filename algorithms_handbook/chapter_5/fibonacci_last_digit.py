def fibonacci_last_digit(n: int) -> int:
    if n <= 1:
        return n
    else:
        old_prev = 0
        prev = 1

        for i in range(n - 1):
            tmp = old_prev
            old_prev = prev
            prev += tmp
            prev = prev % 10

        return prev
