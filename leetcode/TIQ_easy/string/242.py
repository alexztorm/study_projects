def isAnagram(s: str, t: str) -> bool:
    letters = {}

    for char in s:
        letters[char] = letters.get(char, 0) + 1

    for char in t:
        if char not in letters.keys():
            return False
        elif letters[char] <= 0:
            return False
        else:
            letters[char] -= 1

    for quantity in letters.values():
        if quantity != 0:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("ab", "a"))
