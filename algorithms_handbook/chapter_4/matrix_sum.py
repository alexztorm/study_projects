def matrix_sum(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    n = len(matrix1)
    m = len(matrix1[0])

    for i in range(n):
        for j in range(m):
            matrix1[i][j] += matrix2[i][j]

    return matrix1
