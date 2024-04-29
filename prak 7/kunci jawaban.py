def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def find_empty_location(board, l):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False


def used_in_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False


def used_in_col(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False


def used_in_box(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


def is_safe(board, row, col, num):
    return not used_in_row(board, row, num) and not used_in_col(board, col, num) and not used_in_box(board, row - row % 3, col - col % 3, num)


def solve_sudoku(board):
    l = [0, 0]

    if not find_empty_location(board, l):
        return True

    row = l[0]
    col = l[1]

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


# Example Sudoku board (0 represents empty cells)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Masukkan angka untuk setiap kotak Sudoku (0 untuk kotak kosong):")
for i in range(9):
    for j in range(9):
        board[i][j] = int(input(f"Masukkan angka untuk kotak ({i+1}, {j+1}): "))

if solve_sudoku(board):
    print("Sudoku solved successfully:")
    print_board(board)
else:
    print("No solution exists.")
