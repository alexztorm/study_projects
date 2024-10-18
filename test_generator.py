from random import randint
# from algorithms_handbook.chapter_6.spice import max_spice


def generate_test(n: int) -> list[list]:
    test = []

    for _ in range(n):
        new_test = []

        k = randint(1, 10)
        w = randint(0, 2 * 10 ** 6)

        new_test.append(k)
        new_test.append(w)

        c_test = []
        w_test = []

        for i in range(k):
            ci = randint(0, 2 * 10 ** 6)
            wi = randint(0, 2 * 10 ** 6)
            c_test.append(ci)
            w_test.append(wi)

        new_test.append(c_test)
        new_test.append(w_test)

        test.append(new_test)

    return test


def max_spice(w: int, weight: list[int], cost: list[int]) -> float:
    if w <= 0 or not weight:
        return 0

    max_cost, max_cost_id = 0, 0

    for i in range(len(cost)):
        if max_cost < (cost[i] / weight[i]):
            max_cost = cost[i] / weight[i]
            max_cost_id = i

    amount = min(weight[max_cost_id], w)

    revenue = amount * max_cost

    weight.pop(max_cost_id)
    cost.pop(max_cost_id)

    return revenue + max_spice(w - amount, weight, cost)


test1 = generate_test(10)

for block in test1:
    print("n = ", block[0], " w = ", block[1])
    # for i in range(block[0]):
    #    print(f'c_{i} = ', block[2][i], f'w_{i} = ', block[3][i])
    print('res of test = ', '{:.3f}'.format(max_spice(block[1], block[2], block[3])))

