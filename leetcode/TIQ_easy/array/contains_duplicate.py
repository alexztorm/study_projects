def containsDuplicate(nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    else:
        return True


def containsDuplicate2(nums: list[int]) -> bool:
    for i in range(len(nums)):
        if nums[i] in nums[:i]:
            return True
    return False


print(containsDuplicate2([1, 2, 3, 1]))
print(containsDuplicate2([1, 2, 3, 4]))
print(containsDuplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
