
# Minimax Algorithm - Tic Tac Toe

board = [" "] * 9

# Display Board
def print_board():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])


# Check Winner
def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# Minimax Function
def minimax(is_maximizing):
    result = check_winner()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "Draw":
        return 0

    if is_maximizing:
        best_score = -999

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 999

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


# Find Best Move for AI
def best_move():
    best_score = -999
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    return move


# Main Game
print("Tic Tac Toe")
print("You = X, AI = O")

while True:
    print_board()

    position = int(input("Enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid or occupied position!")
        continue

    board[position] = "X"

    if check_winner():
        break

    move = best_move()
    board[move] = "O"

    if check_winner():
        break

print_board()

winner = check_winner()

if winner == "Draw":
    print("Game Draw!")
else:
    print("Winner:", winner)
