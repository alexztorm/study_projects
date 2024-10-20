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

def isPalindrome2(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


print(isPalindrome2("A man, a plan, a canal: Panama"))
print(isPalindrome2("race a car"))
print(isPalindrome2("!!!"))
print(isPalindrome2(" "))
print(isPalindrome2("Marge, let's \"[went].\" I await {news} telegram."))
