def chair_bed(n: int, H: int, h_list: list[int], w_list: list[int]) -> int:
    if n <= 1:
        return 0

    queue = []
    deque_diff = []
    min_dif = max(h_list)
    cur_width = 0
    difs = [0]

    chairs = sorted(zip(h_list, w_list))
    # print(list(chairs))

    k = 0
    for i in range(n):
        queue.append(chairs[i])

        if len(queue) <= 1:
            deque_diff.append((0, i))
        else:
            while deque_diff and deque_diff[-1][0] < (chairs[i][0] - chairs[i - 1][0]):
                deque_diff.pop()
            deque_diff.append((chairs[i][0] - chairs[i - 1][0], i - 1))

        cur_width += chairs[i][1]

        # print(queue, cur_width, min_dif, deque_diff)
        while cur_width >= H:
            if len(queue) == 1:
                return 0
            min_dif = min(min_dif, deque_diff[0][0])
            cur_width -= queue[0][1]
            excluded = queue.pop(0)

            if chairs[deque_diff[0][1]] == excluded:
                deque_diff.pop(0)

            # print(queue, cur_width, min_dif, deque_diff)

    return min_dif


a, b = map(int, input().split())
h = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]

print(chair_bed(a, b, h, w))

# print(chair_bed(4, 7, [1, 4, 1, 2], [1, 4, 2, 3]))  # 2
# print(chair_bed(5, 6, [1, 3, 5, 4, 2], [5, 4, 3, 2, 1]))    # 1
# print(chair_bed(1, 3, [3], [3]))    # 0
# print(chair_bed(5, 6, [3, 3, 3, 3, 3], [5, 4, 3, 2, 1]))    # 0
# print(chair_bed(5, 6, [1, 3, 5, 4, 2], [4, 4, 4, 4, 4]))    # 1
# print(chair_bed(5, 9, [1, 5, 8, 7, 2], [1, 4, 3, 2, 1]))    # 2
# print(chair_bed(5, 10, [1, 2, 3, 10, 15], [1, 1, 1, 5, 5]))  # 5
# print(chair_bed(6, 15, [2, 5, 7, 8, 1, 1], [1, 1, 4, 2, 3, 6]))  # 3
# print(chair_bed(6, 8, [1, 7, 8, 13, 14, 18], [2, 2, 2, 2, 2, 2]))  # 5
# print(chair_bed(5, 9, [1, 3, 6, 5, 2], [3, 4, 3, 2, 1]))  # 2
# print(chair_bed(6, 25, [1, 8, 9, 10, 17, 18, 19], [1, 10, 10, 10, 1, 10, 10]))  # 1
