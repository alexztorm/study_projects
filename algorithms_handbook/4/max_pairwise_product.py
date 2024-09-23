def max_pairwise_product(numbers):
    n = len(numbers)
    numbers.sort()
    return numbers[n-1] * numbers[n-2]


m = int(input())
num_list = input().split(" ")
num_list = [int(x) for x in num_list]

ans = max_pairwise_product(num_list)

print(ans)
