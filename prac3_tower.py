
# Tower of Hanoi using State Space Search

def hanoi(n, source, auxiliary, destination):

    # Goal state
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    # Move n-1 disks to auxiliary rod
    hanoi(n-1, source, destination, auxiliary)

    # Move largest disk to destination
    print("Move disk", n, "from", source, "to", destination)

    # Move n-1 disks to destination rod
    hanoi(n-1, auxiliary, source, destination)


# Number of disks
n = 3

print("Tower of Hanoi Solution:")
hanoi(n, 'A', 'B', 'C')
