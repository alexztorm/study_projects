def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    zero_id = -1
    i = 0

    while i < len(nums):
        # print(nums, i, zero_id)
        if nums[i] == 0 and zero_id == -1:
            zero_id = i
            i += 1
        elif nums[i] != 0 and zero_id != -1:
            nums[zero_id], nums[i] = nums[i], nums[zero_id]
            i = zero_id + 1
            zero_id = -1
        else:
            i += 1

    # print(nums)


def moveZeroes2(nums: list[int]) -> None:
    left = 0

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[right], nums[left] = nums[left], nums[right]
            left += 1


moveZeroes2([0, 1, 3, 0, 12])
moveZeroes2([0])
moveZeroes2([0, 0, 3, 12, 45])
