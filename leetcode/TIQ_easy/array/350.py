from collections import Counter


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


def intersect2(nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []

    hash_map = Counter(nums1)

    for num in nums2:
        if num in hash_map and hash_map[num] > 0:
            ans.append(num)
            hash_map[num] -= 1

    return ans


print(intersect2([1, 2, 3, 4, 5, 6, 7], [1, 3, 5, 7]))
print(intersect2([1, 2, 2, 1], [2, 2]))
print(intersect2([4, 9, 5], [9, 4, 9, 8, 4]))
