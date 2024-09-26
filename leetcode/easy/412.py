class Solution:
    def fizz_buzz(self, n: int) -> list[str]:
        ans = []

        for i in range(1, n + 1):
            ans_str = ""

            if i % 3 == 0:
                ans_str += "Fizz"

            if i % 5 == 0:
                ans_str += "Buzz"

            if not ans_str:
                ans.append(str(i))
            else:
                ans.append(ans_str)

        return ans


s = Solution()
print(s.fizz_buzz(3))
print(s.fizz_buzz(5))
print(s.fizz_buzz(15))
