
# Goal Stack Planning - Blocks World

# Initial State
state = {
    "A": "table",
    "B": "A",
    "C": "table"
}

# Goal State
goal = {
    "A": "B",
    "B": "C",
    "C": "table"
}

# Function to move a block
def move(block, destination):
    print("Move", block, "to", destination)
    state[block] = destination

# Goal Stack
stack = []

# Add goals to stack
for block in goal:
    stack.append((block, goal[block]))

print("Initial State:", state)
print("\nPlanning...\n")

# Process goals
while stack:
    block, destination = stack.pop()

    if state[block] == destination:
        continue

    # Check destination block
    if destination != "table":

        if state[destination] != "table":
            stack.append((block, destination))
            stack.append((destination, "table"))

        else:
            move(block, destination)

    else:
        move(block, "table")

print("\nFinal State:", state)
print("Goal Achieved!")
