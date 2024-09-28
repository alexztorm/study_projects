def merge_n_sorted_lists(n: int, input_list: list) -> list[int]:
    if n > 1:
        output = merge_two_sorted_lists(input_list[0], input_list[1])

        for i in range(2, n):
            output = merge_two_sorted_lists(output, input_list[i])

        return output

    else:
        return input_list[0]


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
