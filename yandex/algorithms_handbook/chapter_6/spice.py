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


n, cap = map(int, input().split())

weight_list, cost_list = [], []

for _ in range(n):
    a, b = map(int, input().split())
    weight_list.append(b)
    cost_list.append(a)

print("{:.3f}".format(max_spice(cap, weight_list, cost_list)))
