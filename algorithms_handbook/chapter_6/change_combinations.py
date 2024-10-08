def change_combinations(n: int) -> list[list[int]]:
    comb = [[0]]

    comb.append(optimal_change(n))
    comb[0][0] += 1
    
    i = 1
    while (10 in new_comb or 5 in new_comb) and i < len(new_comb):
        if new_comb[i] == 10:
            new_comb.pop(i)
            new_comb += [5, 5]
            new_comb[0] += 1
            comb.append(new_comb+[])
            comb[0][0] += 1
        elif new_comb[i] == 5:
            new_comb.pop(i)
            new_comb += [1, 1, 1, 1, 1]
            new_comb[0] += 4
            comb.append(new_comb+[])
            comb[0][0] += 1
        else:
            i += 1
        # print(i, comb)

    for i in range(comb[0][0]):
        if 10 in comb[i] and 5 in comb[i]:
            new_comb = comb[i]+[]
            j = 1
            while j < new_comb[0]:
                if new_comb[j] == 5:
                    new_comb.pop(j)
                    new_comb += [1, 1, 1, 1, 1]
                    new_comb[0] += 4
                    comb.append(new_comb + [])
                    comb[0][0] += 1
                else:
                    j += 1
                # print(j, new_comb)
    return comb


def optimal_change(money):
    coins = [0]
    while money > 0:
        if money >= 10:
            money -= 10
            coins.append(10)
        elif money >= 5:
            money -= 5
            coins.append(5)
        else:
            money -= 1
            coins.append(1)
        coins[0] += 1
    return coins


m = int(input())

ans = change_combinations(m)
for line in ans:
    for el in line:
        print(el, end=" ")
    print("")
