def best_rest(n: int, k: int, numbers: list[int]) -> int:
    ...


a, b = map(int, input().split())
nums = [int(x) for x in input().split()]

print(best_rest(a, b, nums))
