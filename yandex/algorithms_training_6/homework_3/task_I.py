def crossroad(n: int, mr1: int, mr2: int, dist: list[int], time: list[int]) -> list[int]:
    res = [0] * n

    queues = [[], [], [], []]

    ids = list(range(0, n))
    dist_time = sorted(zip(dist, time, ids), key=lambda x: x[1])

    print(dist_time)

    for rover in dist_time:
        queues[rover[0] - 1].append(rover)

    if abs(mr2 - mr1) == 2:
        straight_road = True
    else:
        straight_road = False

    nmr1, nmr2 = -1, -1
    for i in range(4):
        if mr1 != i + 1 or mr2 != i + 1:
            ...
    
    cur_time = min(time) - 1

    while queues[0] or queues[1] or queues[2] or queues[3]:
        break
        cur_time += 1
        if straight_road:
            if queues[mr1 - 1] or queues[mr2 - 1]:
                if queues[mr1 - 1]:
                    res[queues[mr1 - 1][0][2]] = cur_time
                    queues[mr1 - 1].pop(0)
                if queues[mr2 - 1]:
                    res[queues[mr2 - 1][0][2]] = cur_time
                    queues[mr2 - 1].pop(0)
            else:
                ...
        else:
            ...

    return res


# m = int(input())
# m1, m2 = map(int, input().split())
#
# d, t = [], []
# for _ in range(m):
#     a, b = map(int, input().split())
#     d.append(a)
#     t.append(a)
#
# ans = crossroad(m, m1, m2, d, t)

# for item in ans:
#     print(item)

print(crossroad(4, 1, 3, [1, 3, 2, 2], [1, 1, 1, 2]))   #
print(crossroad(4, 1, 3, [1, 2, 3, 2], [1, 1, 1, 2]))   #
print(crossroad(4, 1, 2, [1, 2, 3, 4], [1, 1, 1, 1]))   #
print(crossroad(3, 1, 2, [1, 3, 4], [2, 1, 2]))         #
print(crossroad(4, 1, 3, [1, 3, 2, 2], [1, 1, 7, 8]))   # 1, 1, 7, 8
print(crossroad(2, 1, 3, [2, 2], [1, 1]))   # 1, 2
print(crossroad(2, 1, 2, [2, 1], [1, 7]))   # 1, 7
print(crossroad(2, 1, 2, [2, 1], [1, 1]))   # 2, 1
print(crossroad(4, 1, 3, [2, 4, 2, 4], [1, 1, 1, 1]))   # 1, 1, 2, 2
print(crossroad(4, 1, 3, [1, 3, 1, 3], [2, 2, 1, 1]))   # 2, 2, 1, 1
print(crossroad(1, 1, 3, [2], [95]))   # 95
print(crossroad(2, 1, 3, [2, 4], [95, 107]))   # 95, 107
print(crossroad(2, 1, 3, [2, 4], [107, 95]))   # 107, 95
print(crossroad(4, 4, 1, [4, 1, 1, 2], [1, 1, 4, 1]))   # 1, 2, 4, 3
