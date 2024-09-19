def merge_sort(sorting_list: list[int]) -> list[int]:
    if len(sorting_list) > 1:
        first_half = sorting_list[:len(sorting_list) // 2]
        second_half = sorting_list[len(sorting_list) // 2:]

        sorted_list = merge_two_sorted_lists(merge_sort(first_half), merge_sort(second_half))

        return sorted_list
    else:
        return sorting_list


def merge_two_sorted_lists(first_list: list, second_list: list) -> list[int]:
    i, j = 0, 0
    output = []

    while i < len(first_list) or j < len(second_list):
        if i < len(first_list) and j < len(second_list):
            if first_list[i] < second_list[j]:
                output.append(first_list[i])
                i += 1
            else:
                output.append(second_list[j])
                j += 1
        elif i < len(first_list):
            output.append(first_list[i])
            i += 1
        elif j < len(second_list):
            output.append(second_list[j])
            j += 1

    return output


m = int(input())
num_list = input().split(" ")
num_list = [int(x) for x in num_list]

ans = merge_sort(num_list)

for i in range(m):
    print(ans[i], end=" ")
