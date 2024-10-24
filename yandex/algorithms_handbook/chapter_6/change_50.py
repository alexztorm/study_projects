def change_50(n: int) -> (int, list[int]):
    combination = []
    k = 0

    while n > 0:
        if n >= 50:
            k += 1
            combination.append(50)
            n -= 50
        elif n >= 20:
            k += 1
            combination.append(20)
            n -= 20
        elif n >= 10:
            k += 1
            combination.append(10)
            n -= 10
        elif n >= 5:
            k += 1
            combination.append(5)
            n -= 5
        else:
            k += 1
            combination.append(1)
            n -= 1

    return k, combination


m = int(input())

ans, ans_comb = change_50(m)

print(ans)
for el in ans_comb:
    print(el, end=" ")
