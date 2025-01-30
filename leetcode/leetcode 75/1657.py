from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    word1_dict = Counter(word1)
    word2_dict = Counter(word2)

    for key1 in word1_dict.keys():
        if not word2_dict[key1]:
            return False

    return Counter(word1_dict.values()) == Counter(word2_dict.values())


def closeStrings2(word1: str, word2: str) -> bool:
    word1_dict = Counter(word1)
    word2_dict = Counter(word2)

    print(word1_dict.values(), word2_dict.values())

    for key1 in word1_dict.keys():
        if not word2_dict[key1]:
            return False

    new_word1 = list(word1_dict.values())
    new_word2 = list(word2_dict.values())

    new_word1.sort()
    new_word2.sort()

    if new_word1 == new_word2:
        return True
    else:
        return False


if __name__ == '__main__':
    print(closeStrings("abc", "bca"))
    print(closeStrings("a", "aa"))
    print(closeStrings("cabbba", "abbccc"))
    print(closeStrings("bbbccc", "cccbbb"))
    print(closeStrings("abbzccca", "babzzczc"))
