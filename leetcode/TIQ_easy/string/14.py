def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""

    min_element = min(strs, key=len)

    for i in range(len(min_element)):
        for j in range(len(strs)):
            if strs[j][i] != min_element[i]:
                return prefix
        prefix += min_element[i]

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["park", "parker", "par"]))
