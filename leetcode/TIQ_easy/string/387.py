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


print(firstUniqChar("leetcode"))
print(firstUniqChar("loveleetcode"))
print(firstUniqChar("aabb"))
