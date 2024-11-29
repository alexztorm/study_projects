def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    if n > 0:
        first, second = 0, 0
        excluded = []

        while first < m and second < n:
            print(nums1, excluded, first, second)
            if excluded:
                next_num = min(nums1[first], nums2[second], excluded[0])

                if nums2[second] == next_num:
                    excluded.append(nums1[first])
                    nums1[first] = nums2[second]
                    second += 1
                elif excluded[0] == next_num:
                    excluded.append(nums1[first])
                    nums1[first] = excluded[0]
                    excluded.pop(0)
            else:
                if nums1[first] > nums2[second]:
                    excluded.append(nums1[first])
                    nums1[first] = nums2[second]
                    second += 1
            first += 1

        print(nums1, excluded, first, second)

        while first < m:
            if nums1[first] > excluded[0]:
                excluded.append(nums1[first])
                nums1[first] = excluded[0]
                excluded.pop(0)
            first += 1

        print(nums1, excluded, first, second)

        while second < n:
            if not excluded or nums2[second] <= excluded[0]:
                nums1[first] = nums2[second]
                second += 1
            else:
                nums1[first] = excluded[0]
                excluded.pop(0)
            first += 1

        if excluded:
            nums1[first:] = excluded

    print(nums1)


# merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([1], 1, [], 0)
# merge([0], 0, [1], 1)
# merge([5, 7, 10, 0, 0, 0, 0, 0], 3, [1, 4, 8, 9, 10], 5)
# merge([7, 8, 9, 0, 0, 0], 3, [2, 5, 6], 3)
# merge([1, 0], 1, [2], 1)
merge([1, 2, 4, 5, 6, 0], 5, [3], 1)
