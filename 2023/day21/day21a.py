import sys

from functools import cache

input = open(sys.argv[1]).read()
lines = input.strip().split("\n")
grid = [[c for c in line] for line in lines]

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'S':
            start = (row, col, 0)

results = set()

@cache
def f(node_row, node_col, node_dist):
    if not (0 <= node_row < len(grid) and 0 <= node_col < len(grid[0])):
        return
    if grid[node_row][node_col] == '#':
        return

    if node_dist == 64:
        results.add((node_row, node_col))
        return

    f(node_row + 1, node_col, node_dist + 1)
    f(node_row - 1, node_col, node_dist + 1)
    f(node_row, node_col + 1, node_dist + 1)
    f(node_row, node_col - 1, node_dist + 1)

f(start[0], start[1], start[2])
print(len(results))
