def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()
    return numbers[n-1] * numbers[n-2]
