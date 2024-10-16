def reverseString(s: list[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

    print(s)


reverseString(["h", 'e', "l", "l", "o"])
reverseString(["H", "a", "n", "n", "a", 'h'])
