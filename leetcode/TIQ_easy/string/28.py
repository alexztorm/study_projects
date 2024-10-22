def strStr(haystack: str, needle: str) -> int:
    if haystack == needle:
        return 0

    m = len(needle)

    for i in range(len(haystack) - m + 1):
        if haystack[i:i + m] == needle:
            return i

    return -1


print(strStr("sadbutsade", "ade"))
print(strStr("leetcode", "leeto"))
print(strStr("abc", "c"))
