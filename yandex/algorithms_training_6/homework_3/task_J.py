def chair_bed(n: int, H: int, h_list: list[int], w_list: list[int]) -> int:
    ...


a, b = map(int, input().split())
h = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

print(chair_bed(a, b, h, w))

print(chair_bed(4, 7, [1, 4, 1, 2], [1, 4, 2, 3]))
print(chair_bed(5, 6, [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]))
