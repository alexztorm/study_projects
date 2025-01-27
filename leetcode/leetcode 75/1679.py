def maxOperations(nums: list[int], k: int) -> int:
    ops = 0
    d = {}

    for i in range(len(nums)):
        if nums[i] in d.keys():
            d[nums[i]] += 1
        else:
            d[nums[i]] = 1

    for i in range(len(nums)):
        if k - nums[i] == nums[i]:
            if d[nums[i]] > 1:
                ops += 1
                d[nums[i]] -= 2
        elif (k - nums[i]) in d.keys() and d[k - nums[i]] > 0 and d[nums[i]] > 0:
            ops += 1
            d[k - nums[i]] -= 1
            d[nums[i]] -= 1

    return ops


def maxOperations2(nums: list[int], k: int) -> int:
    operations = 0
    nums.sort()

    left, right = 0, len(nums) - 1
    while left < right:
        cur_sum = nums[left] + nums[right]
        if cur_sum < k:
            left += 1
        elif cur_sum == k:
            operations += 1
            left += 1
            right -= 1
        else:
            right -= 1

    return operations


if __name__ == '__main__':
    print(True if maxOperations([1, 2, 3, 4], 5) == 2 else maxOperations([1, 2, 3, 4], 5))
    print(True if maxOperations([3, 1, 3, 4, 3], 6) == 1 else maxOperations([3, 1, 3, 4, 3], 6))
