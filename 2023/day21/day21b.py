import sys

input = open(sys.argv[1]).read()
lines = input.strip().split("\n")
grid = [[c for c in line] for line in lines]

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'S':
            start = (row, col, 0)

results = set()

dot_countodd = 0
dot_counteven = 0
for i, line in enumerate(grid):
    for j, c in enumerate(line):
        if c != '#':
            if (i + j) % 2 == 0:
                dot_counteven += 1
            else:
                dot_countodd += 1

# min 130 to get to corners
a = False

def f2(node_row, node_col, node_dist, target):
    global results
    global C
    results = set()
    C = set()

    f(node_row, node_col, node_dist, target)

    return len(results)

C = set()

def f(node_row, node_col, node_dist, target):
    if not (0 <= node_row < len(grid) and 0 <= node_col < len(grid[0])):
        return

    if grid[node_row][node_col] == '#':
        return

    if (node_row, node_col, node_dist, target) in C:
        return

    global results
    if node_dist == target:
        results.add((node_row, node_col))
        return

    C.add((node_row, node_col, node_dist, target))

    f(node_row + 1, node_col, node_dist + 1, target)
    f(node_row - 1, node_col, node_dist + 1, target)
    f(node_row, node_col + 1, node_dist + 1, target)
    f(node_row, node_col - 1, node_dist + 1, target)

results = set()
f(start[0], start[1], start[2], len(grid))
grid_temp = [[c for c in line] for line in grid]
for thing in results:
    grid_temp[thing[0]][thing[1]] = 'O'

results = set()
f(start[0], start[1], start[2], len(grid) + 1)
grid_temp2 = [[c for c in line] for line in grid]
for thing in results:
    grid_temp2[thing[0]][thing[1]] = 'O'

dot_countodd = 0
dot_counteven = 0
for line in grid_temp:
    for c in line:
        if c == 'O':
            dot_counteven += 1

for line in grid_temp2:
    for c in line:
        if c == 'O':
            dot_countodd += 1

value = 26501365
checks = (value - len(grid) // 2) // len(grid)

ans = 0

for i in range(0, checks):
    if i % 2 == 0:
        ans += dot_counteven * max(1, i * 4)
    else:
        ans += dot_countodd * max(1, i * 4)

straight_distance = len(grid) // 2 * 2
inner_edge_distance = len(grid) // 2 - 1 + len(grid)
outer_edge_distance = len(grid) // 2 - 1

# left
ans += f2(len(grid) // 2, len(grid) - 1, 0, straight_distance)

# top left
ans += f2(len(grid) - 1, len(grid) - 1, 0, outer_edge_distance) * checks
ans += f2(len(grid) - 1, len(grid) - 1, 0, inner_edge_distance) * (checks - 1)

# bottom
ans += f2(0, len(grid) // 2, 0, straight_distance)

# bottom left
ans += f2(0, len(grid) - 1, 0, outer_edge_distance) * checks
ans += f2(0, len(grid) - 1, 0, inner_edge_distance) * (checks - 1)

# right
ans += f2(len(grid) // 2, 0, 0, straight_distance)

# bottom right
ans += f2(0, 0, 0, outer_edge_distance) * checks
ans += f2(0, 0, 0, inner_edge_distance) * (checks - 1)

# top
ans += f2(len(grid) - 1, len(grid) // 2, 0, straight_distance)

# top right
ans += f2(len(grid) - 1, 0, 0, outer_edge_distance) * checks
ans += f2(len(grid) - 1, 0, 0, inner_edge_distance) * (checks - 1)

print(ans)
