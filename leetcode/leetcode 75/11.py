def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        max_area = max(max_area, min(height[right], height[left]) * (right - left))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


if __name__ == '__main__':
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(maxArea([1, 1]))
