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


s = Solution()
print(s.number_of_steps(14))
print(s.number_of_steps(8))
print(s.number_of_steps(123))
