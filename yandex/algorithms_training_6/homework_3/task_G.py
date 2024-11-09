def pvz_queue(n: int, b: int, a_list: list[int]) -> int:
    time, cur_visitors = 0, 0

    for i in range(n):
        cur_visitors += a_list[i]
        time += cur_visitors
        cur_visitors -= min(cur_visitors, b)

    time += cur_visitors

    return time


m, c = map(int, input().split())
a = [int(x) for x in input().split()]

print(pvz_queue(m, c, a))

# print(pvz_queue(3, 4, [1, 5, 9]))
# print(pvz_queue(5, 3, [2, 5, 7, 9, 11]))
# print(pvz_queue(1, 3, [17]))
# print(pvz_queue(5, 1, [2, 5, 7, 9, 11]))
# print(pvz_queue(3, 1, [3, 2, 4]))
