def findKthLargest(nums: list[int], k: int) -> int:
    # idea by niits
    min_el, max_el = min(nums), max(nums)

    counts = [0] * (max_el - min_el + 1)

    for i in range(len(nums)):
        counts[nums[i] - min_el] += 1

    remaining = k
    i = max_el - min_el

    while remaining > 0:
        remaining -= counts[i]
        i -= 1

    return i + min_el + 1


if __name__ == '__main__':
    print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # 5
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))  # 4
    print(findKthLargest([3, 11, 11, 7, 1, 9], 6))  # 1
    print(findKthLargest([1, 1, 1, 1, 1, 1], 3))  # 1
    print(findKthLargest([7, 6, 5, 4, 3, 2, 1], 2))  # 6
    print(findKthLargest([5, 2, 4, 1, 3, 6, 0], 2))  # 5
    print(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6, 7, 7, 8, 2, 3, 1, 1, 1, 10, 11, 5, 6, 2, 4, 7, 8, 5, 6], 20))  # 2
