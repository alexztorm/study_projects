def productExceptSelf(nums: list[int]) -> list[int]:
    # solution by niits
    output = [1] * len(nums)

    left = 1
    for i in range(len(nums)):
        output[i] *= left
        left *= nums[i]

    right = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= right
        right *= nums[i]

    return output

def productExceptSelf2(nums: list[int]) -> list[int]:
    ans = [0] * len(nums)

    all_product = 1
    zero_count, last_zero_id = 0, -1

    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
            last_zero_id = i
        else:
            all_product *= nums[i]

    if zero_count > 1:
        return ans
    elif zero_count == 1:
        ans[last_zero_id] = all_product
    else:
        for i in range(len(nums)):
            ans[i] = int(all_product / nums[i])

    return ans


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))
    print(productExceptSelf([-1, 1, 0, -3, 3]))
    print(productExceptSelf([-1, 1, 0, 0, 3]))
