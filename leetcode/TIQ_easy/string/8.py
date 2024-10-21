def myAtoi(s: str) -> int:
    i = 0
    is_positive = True
    int_start, int_end = -1, -1
    borders = [str(-2 ** 31), str(2 ** 31 - 1)]

    while i < len(s):
        if s[i] == ' ':
            i += 1
        else:
            break

    if i < len(s):
        if s[i] == '-':
            is_positive = False
            i += 1
        elif s[i] == '+':
            i += 1

    while i < len(s) and s[i].isdigit():
        if s[i] == '0':
            i += 1
        else:
            int_start = i
            int_end = i
            i += 1
            break

    while i < len(s) and s[i].isdigit():
        int_end = i
        i += 1

    new_int = s[int_start:int_end + 1]

    if new_int:
        if is_positive:
            if len(new_int) > len(borders[1]):
                return 2 ** 31 - 1
            elif len(new_int) == len(borders[1]):
                for i in range(len(new_int)):
                    if int(new_int[i]) > int(borders[1][i]):
                        return 2 ** 31 - 1
                    elif int(new_int[i]) < int(borders[1][i]):
                        break

            return int(new_int)
        else:
            if len(new_int) > len(borders[0]) - 1:
                return - 2 ** 31
            elif len(new_int) == len(borders[0]) - 1:
                for i in range(len(new_int)):
                    if int(new_int[i]) > int(borders[0][i + 1]):
                        return - 2 ** 31
                    elif int(new_int[i]) < int(borders[0][i + 1]):
                        break

            return int("-" + new_int)
    else:
        return 0


# print(myAtoi("42"))
# print(myAtoi("-042"))
# print(myAtoi("1337c0d3"))
# print(myAtoi("3-1"))
# print(myAtoi("words and 987"))
# print(myAtoi("-91283472332"))
print(myAtoi(" 1175109307q7"))
