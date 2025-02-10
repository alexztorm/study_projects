def isPowerOfThree(n: int) -> bool:
    return n > 0 and 1162261467 % n == 0


def isPowerOfThree2(n: int) -> bool:
    if n == 0:
        return False

    while n != 1:
        if n % 3 == 0:
            n = n / 3
        else:
            return False
    return True


if __name__ == '__main__':
    print(isPowerOfThree(27))
    print(isPowerOfThree(0))
    print(isPowerOfThree(-1))
    print(isPowerOfThree(1))
