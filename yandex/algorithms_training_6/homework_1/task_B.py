from random import sample


def shirts_n_socks(a: int, b: int, c: int, d: int):
    if a == 0:
        return 1, c + 1
    elif b == 0:
        return 1, d + 1
    elif c == 0:
        return a + 1, 1
    elif d == 0:
        return b + 1, 1
    elif a + c < b + d:
        return a + 1, c + 1
    else:
        return b + 1, d + 1


# input_list = []

# for i in range(4):
#     input_list.append(int(input()))

# x, y = shirts_n_socks(input_list[0], input_list[1], input_list[2], input_list[3])
# print(x, y)

for i in range(100):
    test = sample(range(10), 4)
    x, y = shirts_n_socks(test[0], test[1], test[2], test[3])
    print(test, x, y)
