def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    if k >= n:
        k = k % n

    tmp = nums[n - k:]
    for j in range(n - 1, k - 1, -1):
        nums[j] = nums[j - k]
    nums[:k] = tmp

    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
rotate([-1, -100, 3, 99], 2)
