 
def dfs(a, b, visited, path):

    if b == 2:
        path.append((a, b))
        return True

    if (a, b) in visited:
        return False

    visited.add((a, b))
    path.append((a, b))

    # Fill Jug A
    if dfs(4, b, visited, path):
        return True

    # Fill Jug B
    if dfs(a, 3, visited, path):
        return True

    # Empty Jug A
    if dfs(0, b, visited, path):
        return True

    # Empty Jug B
    if dfs(a, 0, visited, path):
        return True

    # Pour A into B
    amount = min(a, 3 - b)
    if dfs(a - amount, b + amount, visited, path):
        return True

    # Pour B into A
    amount = min(b, 4 - a)
    if dfs(a + amount, b - amount, visited, path):
        return True

    path.pop()
    return False


path = []

if dfs(0, 0, set(), path):
    print("Solution found:")
    for state in path:
        print("Jug A =", state[0], " Jug B =", state[1])
else:
    print("No solution")
