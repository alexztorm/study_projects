def reverse(x: int) -> int:
    borders = [str(-2**31), str(2**31-1)]

    s = list(str(x))
    handle_minus = None

    if s[0] == "-":
        handle_minus = s.pop(0)

    print(s)

    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)

    if handle_minus:
        s = "-" + "".join(s)

        if len(s) > len(borders[0]):
            return 0
        elif len(s) == len(borders[0]):
            for i in range(1, len(s)):
                print(s[i], borders[0][i])
                if int(s[i]) > int(borders[0][i]):
                    return 0
                elif int(s[i]) < int(borders[0][i]):
                    break
    else:
        s = "".join(s)

        if len(s) > len(borders[1]):
            return 0
        elif len(s) == len(borders[1]):
            for i in range(len(s)):
                if int(s[i]) > int(borders[1][i]):
                    return 0

    return int(s)


def reverse2(x: int) -> int:
    if x == -2**31:
        return 0

    is_negative = False
    if x < 0:
        is_negative = True
        x *= -1

    res = 0
    while x > 0:
        digit = x % 10
        x //= 10
        if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
            return 0
        res = (res * 10) + digit

    return -res if is_negative else res


print(reverse2(901000))
print(reverse2(-123))
print(reverse2(120))
print(reverse2(-2147483412))
print(reverse2(-2**31))
print(reverse2(2**32))
