class Solution:
    def maximum_wealth(self, accounts: list[list[int]]) -> int:
        max_wealth = sum(accounts[0])

        for i in range(1, len(accounts)):
            if sum(accounts[i]) > max_wealth:
                max_wealth = sum(accounts[i])

        return max_wealth


s = Solution()

print(s.maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(s.maximum_wealth([[1, 5], [7, 3], [3, 5]]))
print(s.maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
