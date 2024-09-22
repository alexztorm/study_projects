def matrix_sum(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    n = len(matrix1)
    m = len(matrix1[0])

    for i in range(n):
        for j in range(m):
            matrix1[i][j] += matrix2[i][j]

    return matrix1


n, m = map(int, input().split())

m1, m2 = [], []

for i in range(n):
    line = input().split(" ")
    line = [int(x) for x in line]
    m1.append(line)

for i in range(n):
    line = input().split(" ")
    line = [int(x) for x in line]
    m2.append(line)

ans = matrix_sum(m1, m2)

for i in range(n):
    for j in range(m):
        print(ans[i][j], end=" ")
    print("")
