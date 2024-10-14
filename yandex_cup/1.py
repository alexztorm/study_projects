import math


def two_of_three(a, b, c, n):
    left, right = 1, 10**18
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if count_numbers(a, b, c, mid) >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result


def lcm(a, b):
    return (a * b) // math.gcd(a, b)


def count_numbers(a, b, c, n):
    lcm_ab = lcm(a, b)
    lcm_bc = lcm(b, c)
    lcm_ca = lcm(c, a)
    lcm_abc = lcm(lcm_ab, c)

    count = (n // lcm_ab) + (n // lcm_bc) + (n // lcm_ca) - 2 * (n // lcm_abc)
    return count


a, b, c = map(int, input().split())
n = int(input())

answer = two_of_three(a, b, c, n + 1)
print(answer)
