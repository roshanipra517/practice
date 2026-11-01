 
from heapq import heappush, heappop

# Goal State
goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Calculate Heuristic (Misplaced Tiles)
def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


# Find Blank Tile Position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate Next States
def get_neighbors(state):
    neighbors = []

    x, y = find_blank(state)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            neighbors.append(new_state)

    return neighbors


# A* Algorithm
def a_star(start):
    pq = []

    heappush(pq, (heuristic(start), 0, start))

    visited = set()

    while pq:
        f, g, current = heappop(pq)

        state_tuple = tuple(map(tuple, current))

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        print("\nCurrent State:")
        for row in current:
            print(row)

        if current == goal:
            print("\nGoal Reached!")
            return

        for neighbor in get_neighbors(current):
            state_tuple = tuple(map(tuple, neighbor))

            if state_tuple not in visited:
                h = heuristic(neighbor)
                heappush(pq, (g + 1 + h, g + 1, neighbor))

    print("No solution found!")


# Input Initial State
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Call A* Algorithm
a_star(start)
