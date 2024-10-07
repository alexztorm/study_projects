def containsDuplicate(nums: list[int]) -> bool:
    if len(nums) == len(set(nums)):
        return False
    else:
        return True


print(containsDuplicate([1, 2, 3, 1]))
print(containsDuplicate([1, 2, 3, 4]))
print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
