def delete_medians(n: int, numbers: list[int]) -> list[int]:
    ans = []

    numbers.sort()

    if n % 2 == 0:
        left = n // 2 - 1
        right = n // 2
    else:
        ans.append(numbers[n // 2])
        left = n // 2 - 1
        right = n // 2 + 1

    while left > -1 and right < n:
        if numbers[left] <= numbers[right]:
            ans.append(numbers[left])
            ans.append(numbers[right])
        else:
            ans.append(numbers[right])
            ans.append(numbers[left])
        left -= 1
        right += 1

    while left > -1:
        ans.append(numbers[left])
        left -= 1

    while right < n:
        ans.append(numbers[right])
        right += 1

    return ans


m = int(input())
nums = [int(x) for x in input().split()]

res = delete_medians(m, nums)

for item in res:
    print(item, end=' ')


