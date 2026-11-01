
# BFS for Robot Path Planning

from collections import deque

# Grid
grid = [
    ['S', 0, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 0, 0, 'G']
]

# Find start and goal
start = (0, 0)
goal = (3, 3)

# Possible movements: Up, Down, Left, Right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(start, goal):

    queue = deque([start])
    visited = [start]
    parent = {}

    while queue:

        current = queue.popleft()

        # Check goal
        if current == goal:

            path = []

            while current != start:
                path.append(current)
                current = parent[current]

            path.append(start)
            path.reverse()

            return path

        # Check all possible movements
        for move in moves:

            row = current[0] + move[0]
            col = current[1] + move[1]

            # Check grid boundary
            if 0 <= row < 4 and 0 <= col < 4:

                # Avoid obstacles
                if grid[row][col] != 1:

                    next_position = (row, col)

                    if next_position not in visited:

                        visited.append(next_position)
                        parent[next_position] = current
                        queue.append(next_position)

    return None


# Run BFS
path = bfs(start, goal)

if path:
    print("Path Found!")
    print("Path:", path)
    print("Total Moves:", len(path) - 1)

else:
    print("No Path Found!")
