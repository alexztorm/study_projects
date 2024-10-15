def rotate(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)

    for i in range(n - 1):
        for j in range(i, n - 1 - i):
            matrix = one_rotation(matrix, (i, j))

    print(matrix)


def one_rotation(matrix: list[list[int]], start: tuple[int, int]) -> list[list[int]]:
    i, j = start[0], start[1]
    n = len(matrix)
    tmp = matrix[i][j]

    for _ in range(3):
        matrix[i][j] = matrix[n - 1 - j][i]
        i, j = n - 1 - j, i

    matrix[i][j] = tmp

    return matrix


rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

