def irregular_string_sum(str1: str, str2: str) -> str:
    n = len(str1)
    output = []

    for i in range(n):
        output.append(str1[i])
        output.append(str2[i])

    return "".join(output)


m = int(input())
line1, line2 = input(), input()

ans = irregular_string_sum(line1, line2)

print(ans)
