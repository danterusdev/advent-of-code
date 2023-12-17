import sys

from collections import deque

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split("\n")]
grid = [[int(c) for c in line] for line in lines]
graph = {}

for r in range(len(grid)):
    for c in range(len(grid[0])):
        neighbors = []

        if r > 0:
            neighbors.append((r - 1, c, grid[r - 1][c]))
        if c > 0:
            neighbors.append((r, c - 1, grid[r][c - 1]))

        if r < len(grid) - 1:
            neighbors.append((r + 1, c, grid[r + 1][c]))
        if c < len(grid[0]) - 1:
            neighbors.append((r, c + 1, grid[r][c + 1]))

        graph[(r, c)] = neighbors

# 1=left, 2=right,3=up,4=down
nodes = deque()
nodes.append((0, 0, 0, 1, 0))
mindistances = {}
while len(nodes) > 0:
    node = nodes.popleft()
    row, col, distance, count, direction = node

    if (row, col, count, direction) not in mindistances or distance < mindistances[(row, col, count, direction)]:
        mindistances[(row, col, count, direction)] = distance

        for (child_r, child_c, child_d) in graph[(row, col)]:
            c_direction = 0
            if child_r < row:
                c_direction = 3
            elif child_r > row:
                c_direction = 4
            elif child_c < col:
                c_direction = 1
            elif child_c > col:
                c_direction = 2
            else:
                assert False

            c_count = 1
            if direction == c_direction:
                c_count += count

            # turning in available space
            if direction == 0 or (count > 3 and count < 11 and ((c_direction in [1, 2] and direction in [3, 4]) or (c_direction in [3, 4] and direction in [1, 2]))):
                nodes.append((child_r, child_c, distance + child_d, c_count, c_direction))

            # going straight in available space
            if direction == 0 or (count < 10 and c_direction == direction):
                nodes.append((child_r, child_c, distance + child_d, c_count, c_direction))

min = 9999999
for key, value in mindistances.items():
    if key[0] == len(grid) - 1 and key[1] == len(grid[0]) - 1:
        print(key, value)
        if value < min and key[2] >= 4:
            min = value

print(min)
