class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i, j = 0, 1
        ans = 1

        while j != len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                ans += 1
            j += 1

        # print(nums)
        return ans


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
