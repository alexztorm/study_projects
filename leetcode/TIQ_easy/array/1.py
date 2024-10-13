def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if target - nums[i] == nums[j]:
                return [i, j]


def twoSum2(nums: list[int], target: int) -> list[int]:
    num_idx = {}
    for i in range(len(nums)):
        if target - nums[i] not in num_idx.keys():
            num_idx[nums[i]] = i
        else:
            return [num_idx[target - nums[i]], i]


print(twoSum2([2, 7, 11, 15], 9))
print(twoSum2([3, 2, 4], 6))
print(twoSum2([3, 3], 6))
