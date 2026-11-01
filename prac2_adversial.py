
# Alpha-Beta Pruning Program

def alphabeta(depth, index, max_player, values, alpha, beta):

    # If leaf node is reached
    if depth == 3:
        return values[index]

    if max_player:
        best = float('-inf')

        # Check two child nodes
        for i in range(2):

            value = alphabeta(depth + 1, index * 2 + i,
                              False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):

            value = alphabeta(depth + 1, index * 2 + i,
                              True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if beta <= alpha:
                break

        return best


# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]

# Call the function
result = alphabeta(0, 0, True, values, float('-inf'), float('inf'))

print("Optimal Value:", result)
