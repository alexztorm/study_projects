def singleNumber(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        nums.sort()

        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]

        if nums[len(nums) - 1] != nums[len(nums) - 2]:
            return nums[len(nums) - 1]


def singleNumber2(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
        print(result)
    return result


print(singleNumber2([2, 2, 1]))
print(singleNumber2([4, 1, 2, 1, 2]))
print(singleNumber2([1]))
