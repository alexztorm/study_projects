def selection_sort(n: int, number_list: list[int]) -> list[int]:
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if number_list[j] < number_list[min_index]:
                min_index = j
        number_list[i], number_list[min_index] = number_list[min_index], number_list[i]

    return number_list


m = int(input())
num_list = input().split(" ")
num_list = [int(x) for x in num_list]

ans = selection_sort(m, num_list)

for i in range(m):
    print(ans[i], end=" ")
