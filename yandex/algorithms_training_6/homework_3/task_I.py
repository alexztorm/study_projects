def crossroad(n: int, mr1: int, mr2: int, dist: list[int], time: list[int]) -> list[int]:
    res = [0] * n

    queues = {1: [], 2: [], 3: [], 4: []}

    ids = list(range(0, n))
    dist_time = sorted(zip(dist, time, ids), key=lambda x: x[1])

    for item in dist_time:
        queues[item[0]].append(item)

    cur_time = -1
    count_rovers = 0
    straight_road = (abs(mr1 - mr2) == 2)
    nmr1, nmr2 = 5 - mr2, 5 - mr1

    if straight_road:
        while count_rovers < n:
            a, b = queues[mr1] and queues[mr1][0][1] <= cur_time, queues[mr2] and queues[mr2][0][1] <= cur_time
            if a or b:
                if a:
                    res[queues[mr1][0][2]] = cur_time
                    queues[mr1].pop(0)
                    count_rovers += 1
                if b:
                    res[queues[mr2][0][2]] = cur_time
                    queues[mr2].pop(0)
                    count_rovers += 1
            else:
                if queues[nmr1] and queues[nmr1][0][1] <= cur_time:
                    res[queues[nmr1][0][2]] = cur_time
                    queues[nmr1].pop(0)
                    count_rovers += 1
                if queues[nmr2] and queues[nmr2][0][1] <= cur_time:
                    res[queues[nmr2][0][2]] = cur_time
                    queues[nmr2].pop(0)
                    count_rovers += 1
            cur_time += 1
    else:
        mult = mr1 * mr2
        if mult == 2:
            prior = [1, 2, 3, 4]
        elif mult == 4:
            prior = [4, 1, 2, 3]
        elif mult == 6:
            prior = [2, 3, 4, 1]
        else:
            prior = [3, 4, 1, 2]

        while count_rovers < n:
            if queues[prior[0]] and queues[prior[0]][0][1] <= cur_time:
                res[queues[prior[0]][0][2]] = cur_time
                queues[prior[0]].pop(0)
                count_rovers += 1
            elif queues[prior[1]] and queues[prior[1]][0][1] <= cur_time:
                res[queues[prior[1]][0][2]] = cur_time
                queues[prior[1]].pop(0)
                count_rovers += 1
            elif queues[prior[2]] and queues[prior[2]][0][1] <= cur_time:
                res[queues[prior[2]][0][2]] = cur_time
                queues[prior[2]].pop(0)
                count_rovers += 1
            elif queues[prior[3]] and queues[prior[3]][0][1] <= cur_time:
                res[queues[prior[3]][0][2]] = cur_time
                queues[prior[3]].pop(0)
                count_rovers += 1
            cur_time += 1

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
# print(crossroad(4, 1, 3, [1, 2, 3, 4], [1, 2, 2, 3]))   # 1, 3, 2, 3
