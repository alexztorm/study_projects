def isPalindrome(s: str) -> bool:
    i = 0
    while s and i < len(s):
        if not s[i].isalnum():
            s = s.replace(s[i], "")
            i -= 1
        i += 1

    s = s.lower()

    # print(s)

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome("!!!"))
print(isPalindrome(" "))
print(isPalindrome("Marge, let's \"[went].\" I await {news} telegram."))
