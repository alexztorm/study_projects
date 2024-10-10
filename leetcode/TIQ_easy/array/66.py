def plusOne(digits: list[int]) -> list[int]:
    i = len(digits) - 1

    while i >= 0:
        if digits[i] == 9:
            digits[i] = 0
            i -= 1
        else:
            digits[i] += 1
            return digits

    digits.insert(0, 1)
    return digits


print(plusOne([1, 2, 3]))
print(plusOne([4, 3, 2, 1]))
print(plusOne([9]))
