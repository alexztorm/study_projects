from gcd import gcd


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


a1, b1 = map(int, input().split())
print(lcm(a1, b1))
