from collections import deque


def longestOnes(nums: list[int], k: int) -> int:
    left, max_len, count_zeros = 0, 0, 0

    for right in range(len(nums)):
        if nums[right] == 0:
            count_zeros += 1
            while count_zeros > k:
                if nums[left] == 0:
                    count_zeros -= 1
                left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


def longestOnes2(nums: list[int], k: int) -> int:
    max_len = 0
    window = deque()
    count_zeros = 0

    for i in range(len(nums)):
        window.append(nums[i])

        if nums[i] == 0:
            count_zeros += 1
            while count_zeros > k:
                excluded = window.popleft()
                if excluded == 0:
                    count_zeros -= 1

        max_len = max(max_len, len(window))

    return max_len


if __name__ == '__main__':
    print(True if longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6 else longestOnes(
        [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2))
    print(True if longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10 else
        longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
