def quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    first = numbers[0]
    num_small, num_large = [], []

    for i in range(1, len(numbers)):
        if numbers[i] < first:
            num_small.append(numbers[i])
        else:
            num_large.append(numbers[i])

    return quick_sort(num_small) + [first] + quick_sort(num_large)


m = int(input())
num_list = input().split(" ")
num_list = [int(x) for x in num_list]

ans = quick_sort(num_list)

for i in range(m):
    print(ans[i], end=" ")
