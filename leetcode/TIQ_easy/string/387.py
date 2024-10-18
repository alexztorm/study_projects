def firstUniqChar(s: str) -> int:
    uniques = []
    for i in range(len(s)):
        if s[i] not in uniques:
            uniques.append(s[i])

    for i in range(len(s)):
        if uniques:
            if s[i] == uniques[0]:
                if s[i] not in s[i+1:]:
                    return i
                else:
                    uniques.pop(0)

    return -1


def firstUniqChar2(s: str) -> int:
    # Solution idea by MarkSPhilip31
    uniques = {}

    for letter in s:
        uniques[letter] = uniques.get(letter, 0) + 1

    for i in range(len(s)):
        if uniques[s[i]] == 1:
            return i

    return -1


print(firstUniqChar2("leetcode"))
print(firstUniqChar2("loveleetcode"))
print(firstUniqChar2("aabb"))
