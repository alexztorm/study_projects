def shirts_n_socks(a: int, b: int, c: int, d: int):
    return min(a, b) + 1, min(c, d) + 1


input_list = []

for i in range(4):
    input_list.append(int(input()))

x, y = shirts_n_socks(input_list[0], input_list[1], input_list[2], input_list[3])
print(x, y)
