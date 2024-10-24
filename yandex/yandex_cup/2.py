def find_slopes(data: list) -> list[int]:
    res = []

    for input_line in data:
        prev = input_line[0]
        for i in range(1, len(input_line)):
            ...

    return res


n = int(input())
input_data = []

for i in range(n):
    k = int(input())
    nums = [int(x) for x in input().split()]
    input_data.append(nums)

ans = find_slopes(input_data)

for el in ans:
    print(el)