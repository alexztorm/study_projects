class Solution:
    def number_of_steps(self, num: int) -> int:
        ans = 0

        while num != 0:
            while num % 2 == 0:
                ans += 1
                num = num / 2
            ans += 1
            num -= 1

        return ans


    def number_of_steps2(self, num: int) -> int:
        ans = 0

        while num != 0:
            while num & 1 == 0:
                ans += 1
                num = num >> 1
            ans += 1
            num -= 1

        return ans


s = Solution()
print(s.number_of_steps2(14))
print(s.number_of_steps2(8))
print(s.number_of_steps2(123))
