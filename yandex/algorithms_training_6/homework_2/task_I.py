def learn_algorithms(n: int, a: list[int], b: list[int], p: list[int]) -> list[int]:
    res = []
    ids = list(range(1, n + 1))
    learned = set()

    list_a = sorted(zip(a, b, ids), reverse=True, key=sort_by_a)
    list_b = sorted(zip(a, b, ids), reverse=True, key=sort_by_b)

    # for i in range(n):
    #     print(list_a[i], list_b[i])

    list_a_it = 0
    list_b_it = 0
    for i in range(n):
        if p[i] == 0:
            while list_a_it < n:
                if list_a[list_a_it] not in learned:
                    res.append(list_a[list_a_it][2])
                    learned.add(list_a[list_a_it])
                    break
                list_a_it += 1
        else:
            while list_b_it < n:
                if list_b[list_b_it] not in learned:
                    res.append(list_b[list_b_it][2])
                    learned.add(list_b[list_b_it])
                    break
                list_b_it += 1

    return res


def sort_by_a(item):
    return item[0] + item[1] / 10 ** 10 - item[2] / 10 ** 11


def sort_by_b(item):
    return item[1] + item[0] / 10 ** 10 - item[2] / 10 ** 11


# m = int(input())
#
# a_i = [int(x) for x in input().split()]
# b_i = [int(x) for x in input().split()]
# p_i = [int(x) for x in input().split()]
#
# ans = learn_algorithms(m, a_i, b_i, p_i)
#
# for num in ans:
#     print(num, end=" ")

print(learn_algorithms(5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 0, 1, 0, 0]))
print(learn_algorithms(6, [3, 10, 6, 2, 10, 1], [3, 5, 10, 7, 5, 9], [0, 0, 1, 1, 0, 1]))
print(learn_algorithms(5, [4, 4, 2, 1, 5], [1, 2, 3, 4, 5], [1, 1, 0, 0, 1]))
print(learn_algorithms(5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [0, 0, 0, 0, 0]))
print(learn_algorithms(5, [1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 1, 1, 1, 1]))
print(learn_algorithms(5, [10, 10, 20, 20, 10], [20, 10, 20, 10, 20], [0, 0, 0, 1, 1]))
print(learn_algorithms(5, [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [1, 0, 1, 0, 0]))
print(learn_algorithms(5, [1, 1, 1, 1, 2], [1, 1, 1, 1, 1], [1, 0, 1, 0, 0]))
print(learn_algorithms(5, [5, 5, 5, 5, 5], [1, 2, 3, 4, 5], [0, 0, 0, 0, 0]))
print(learn_algorithms(5, [3, 5, 3, 5, 3], [5, 3, 5, 3, 5], [0, 0, 0, 0, 0]))
