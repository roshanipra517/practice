N = 8

board = [[0 for i in range(N)] for j in range(N)]

# Check whether queen can be placed safely
def is_safe(row, col):

    # Check upper column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking function
def solve(row):

    if row == N:
        return True

    for col in range(N):

        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Solve the problem
if solve(0):
    print("Solution for 8 Queens:")

    for row in board:
        for col in row:
            if col == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()
else:
    print("Solution does not exist")