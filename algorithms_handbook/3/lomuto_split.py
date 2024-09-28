def lomuto_split(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    i, j = 1, 1

    first = numbers[0]

    while j != len(numbers):
        if numbers[j] < first:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            i += 1
        j += 1

    numbers[0], numbers[i - 1] = numbers[i - 1], numbers[0]

    return lomuto_split(numbers[:i - 1]) + [first] + lomuto_split(numbers[i:])
