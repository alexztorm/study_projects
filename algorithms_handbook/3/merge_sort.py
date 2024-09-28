from merge_sorted_lists import merge_two_sorted_lists


def merge_sort(sorting_list: list[int]) -> list[int]:
    if len(sorting_list) > 1:
        first_half = sorting_list[:len(sorting_list) // 2]
        second_half = sorting_list[len(sorting_list) // 2:]

        sorted_list = merge_two_sorted_lists(merge_sort(first_half), merge_sort(second_half))

        return sorted_list
    else:
        return sorting_list
