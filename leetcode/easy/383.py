class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        letters_available = {}

        for letter in magazine:
            if letter not in letters_available.keys():
                letters_available[letter] = 1
            else:
                letters_available[letter] += 1

        for letter in ransom_note:
            if letter not in letters_available.keys():
                return False
            else:
                letters_available[letter] -= 1
                if letters_available[letter] < 0:
                    return False

        return True


s = Solution()
print(s.can_construct("a", "b"))
print(s.can_construct("aa", "ab"))
print(s.can_construct("aa", "aab"))
