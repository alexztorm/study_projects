def reverseWords(s: str) -> str:
    new_s = s.split(' ')
    new_s = [item for item in new_s if item != '']
    new_s.reverse()
    return ' '.join(new_s)


if __name__ == '__main__':
    print(reverseWords("the sky is blue"), reverseWords("the sky is blue") == "blue is sky the")
    print(reverseWords("  hello world  "), reverseWords("  hello world  ") == "world hello")
    print(reverseWords("a good   example"), reverseWords("a good   example") == "example good a")
