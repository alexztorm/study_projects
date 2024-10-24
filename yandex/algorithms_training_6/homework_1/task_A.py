def raft(x1: int, y1: int, x2: int, y2: int, x: int, y: int):
    ans = ""

    if y > y2:
        ans += "N"
    elif y < y1:
        ans += "S"

    if x > x2:
        ans += "E"
    elif x < x1:
        ans += "W"

    return ans


input_list = []

for i in range(6):
    input_list.append(int(input()))

print(raft(input_list[0], input_list[1], input_list[2], input_list[3], input_list[4], input_list[5]))
print(raft(1, 1, 5, 5, 0, 3) == "W")
print(raft(-3, -3, 5, 5, 6, 3) == "E")
