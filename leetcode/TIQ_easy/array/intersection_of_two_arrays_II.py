def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []

    if len(nums1) < len(nums2):
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                ans.append(nums2.pop(nums2.index(nums1[i])))
    else:
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                ans.append(nums1.pop(nums1.index(nums2[i])))

    return ans


print(intersect([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7]))
print(intersect([1, 2, 2, 1], [2, 2]))
print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
