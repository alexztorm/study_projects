def rob(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    sums = [0] * len(nums)
    sums[0], sums[1] = nums[0], nums[1]

    for i in range(2, len(nums)):
        sums[i] = nums[i] + max(sums[:(i-1)])

    return max(sums[-1], sums[-2])


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]) == 4)
    print(rob([2, 7, 9, 3, 1]) == 12)
    print(rob([1]) == 1)
    print(rob([2, 1, 1, 2]) == 4)
    print(rob([10, 1, 2, 9, 4, 5, 6, 7, 8, 3]))
