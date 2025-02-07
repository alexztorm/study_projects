def findPeakElement(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1

    return left


def findPeakElement2(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[-1] > nums[-2]:
        return len(nums) - 1

    center = int(len(nums) / 2)

    if nums[center - 1] < nums[center] and nums[center] > nums[center + 1]:
        return center
    else:
        print(nums[center - 1], nums[center], nums[center + 1])
        if nums[center - 1] > nums[center + 1]:
            return findPeakElement(nums[:center])
        else:
            print(nums[center + 1:])
            return (center + 1) + findPeakElement(nums[center + 1:])


if __name__ == '__main__':
    print(findPeakElement([1, 2, 3, 1]))
    print(findPeakElement([1, 2, 1, 3, 5, 6, 5]))
    print(findPeakElement([4, 6, 4, 3, 5, 6, 7]))
    print(findPeakElement([4, 6, 4, 3, 1, 1, 1]))
