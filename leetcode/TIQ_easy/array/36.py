def isValidSudoku(board: list[list[str]]) -> bool:
    val_ind = {}

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] not in val_ind.keys():
                    val_ind[board[i][j]] = [[i, j]]
                else:
                    val_ind[board[i][j]].append([i, j])

    for value in val_ind.keys():
        index_list = val_ind[value]
        for i in range(len(index_list)):
            for j in range(i + 1, len(index_list)):
                if index_list[i][0] == index_list[j][0] or index_list[i][1] == index_list[j][1]:
                    return False
                if index_list[i][0] // 3 == index_list[j][0] // 3 and index_list[i][1] // 3 == index_list[j][1] // 3:
                    return False

    return True


print(isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
print(isValidSudoku([[".", "3", ".", ".", "7", ".", ".", ".", "."],
                     ["6", "8", ".", "1", "9", "5", ".", ".", "."],
                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
