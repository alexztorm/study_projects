from fibonacci import fibonacci


def euqlid_max_steps(n: int) -> list[int]:
    old_prev, prev, curr = 0, 0, 0
    counter = 1

    while curr <= n:
        old_prev = prev
        prev = curr
        curr = fibonacci(counter)
        counter += 1

    return [old_prev, prev]
