from random import randint


def random_quick_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    first = randint(0, len(numbers) - 1)
    first_el = numbers[first]
    num_small, num_large = [], []

    for i in range(0, len(numbers)):
        if i != first:
            if numbers[i] < first_el:
                num_small.append(numbers[i])
            else:
                num_large.append(numbers[i])

    return random_quick_sort(num_small) + [first_el] + random_quick_sort(num_large)
