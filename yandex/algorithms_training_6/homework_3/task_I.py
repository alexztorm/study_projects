def crossroad(n: int, mr1: int, mr2: int, dist: list[int], time: list[int]) -> list[int]:
    res = [0] * n

    queues = {1: [], 2: [], 3: [], 4: []}

    ids = list(range(0, n))
    dist_time = sorted(zip(dist, time, ids), key=lambda x: x[1])

    for rover in dist_time:
        queues[rover[0]].append(rover)

    if abs(mr2 - mr1) == 2:
        straight_road = True
    else:
        straight_road = False

    nmr1, nmr2 = -1, -1
    for i in range(4):
        if mr1 != i + 1 and mr2 != i + 1:
            if nmr1 == -1:
                nmr1 = i + 1
            else:
                nmr2 = i + 1

    cur_time = min(time) - 1

    while queues[1] or queues[2] or queues[3] or queues[4]:
        cur_time += 1
        if straight_road:
            if queues[mr1] and queues[mr1][0][1] <= cur_time or queues[mr2] and queues[mr2][0][1] <= cur_time:
                if queues[mr1] and queues[mr1][0][1] <= cur_time:
                    res[queues[mr1][0][2]] = cur_time
                    queues[mr1].pop(0)
                if queues[mr2] and queues[mr2][0][1] <= cur_time:
                    res[queues[mr2][0][2]] = cur_time
                    queues[mr2].pop(0)
            else:
                if queues[nmr1] and queues[nmr1][0][1] <= cur_time:
                    res[queues[nmr1][0][2]] = cur_time
                    queues[nmr1].pop(0)
                if queues[nmr2] and queues[nmr2][0][1] <= cur_time:
                    res[queues[nmr2][0][2]] = cur_time
                    queues[nmr2].pop(0)
        else:
            if queues[mr1] and queues[mr1][0][1] <= cur_time or queues[mr2] and queues[mr2][0][1] <= cur_time:
                if queues[mr1] and queues[mr1][0][1] <= cur_time and (mr1 < mr2 or mr1 == 4 and mr2 == 1):
                    res[queues[mr1][0][2]] = cur_time
                    queues[mr1].pop(0)
                elif queues[mr2] and queues[mr2][0][1] <= cur_time:
                    res[queues[mr2][0][2]] = cur_time
                    queues[mr2].pop(0)
            else:
                if queues[nmr1] and queues[nmr1][0][1] <= cur_time and (nmr1 < nmr2 or nmr1 == 4 and nmr2 == 1):
                    res[queues[nmr1][0][2]] = cur_time
                    queues[nmr1].pop(0)
                elif queues[nmr2] and queues[nmr2][0][1] <= cur_time:
                    res[queues[nmr2][0][2]] = cur_time
                    queues[nmr2].pop(0)

    return res


m = int(input())
m1, m2 = map(int, input().split())

d, t = [], []
for _ in range(m):
    a, b = map(int, input().split())
    d.append(a)
    t.append(b)

ans = crossroad(m, m1, m2, d, t)

for item in ans:
    print(item)

# print(crossroad(4, 1, 3, [1, 3, 2, 2], [1, 1, 1, 2]))   # 1, 1, 2, 3
# print(crossroad(4, 1, 3, [1, 2, 3, 2], [1, 1, 1, 2]))   # 1, 2, 1, 3
# print(crossroad(4, 1, 2, [1, 2, 3, 4], [1, 1, 1, 1]))   # 1, 2, 3, 4
# print(crossroad(3, 1, 2, [1, 3, 4], [2, 1, 2]))         # 2, 1, 3
# print(crossroad(4, 1, 3, [1, 3, 2, 2], [1, 1, 7, 8]))   # 1, 1, 7, 8
# print(crossroad(2, 1, 3, [2, 2], [1, 1]))   # 1, 2
# print(crossroad(2, 1, 2, [2, 1], [1, 7]))   # 1, 7
# print(crossroad(2, 1, 2, [2, 1], [1, 1]))   # 2, 1
# print(crossroad(4, 1, 3, [2, 4, 2, 4], [1, 1, 1, 1]))   # 1, 1, 2, 2
# print(crossroad(4, 1, 3, [1, 3, 1, 3], [2, 2, 1, 1]))   # 2, 2, 1, 1
# print(crossroad(1, 1, 3, [2], [95]))   # 95
# print(crossroad(2, 1, 3, [2, 4], [95, 107]))   # 95, 107
# print(crossroad(2, 1, 3, [2, 4], [107, 95]))   # 107, 95
# print(crossroad(4, 4, 1, [4, 1, 1, 2], [1, 1, 4, 1]))   # 1, 2, 4, 3
# print(crossroad(4, 1, 3, [1, 2, 3, 4], [1, 2, 2, 3]))
