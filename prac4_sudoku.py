
# Sudoku Solver using Backtracking and Constraint Propagation

# 0 represents an empty cell
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


# Check whether a number is valid
def is_valid(board, row, col, num):

    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# Find possible numbers for an empty cell
def candidates(board, row, col):

    possible = []

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            possible.append(num)

    return possible


# Constraint Propagation
def propagate(board):

    changed = True

    while changed:
        changed = False

        for row in range(9):
            for col in range(9):

                if board[row][col] == 0:

                    possible = candidates(board, row, col)

                    if len(possible) == 0:
                        return False

                    # Only one possible number
                    if len(possible) == 1:
                        board[row][col] = possible[0]
                        changed = True

    return True


# Backtracking
def solve(board):

    # Apply constraint propagation
    if not propagate(board):
        return False

    # Find empty cell
    for row in range(9):
        for col in range(9):

            if board[row][col] == 0:

                # Try possible numbers
                possible = candidates(board, row, col)

                for num in possible:

                    new_board = [r[:] for r in board]
                    new_board[row][col] = num

                    if solve(new_board):
                        for i in range(9):
                            board[i] = new_board[i]

                        return True

                return False

    return True


# Print Sudoku
if solve(board):
    print("Sudoku Solved Successfully!")

    for row in board:
        print(row)
else:
    print("No solution exists!")
