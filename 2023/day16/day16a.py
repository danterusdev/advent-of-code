import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split("\n")]
grid = [[c for c in line] for line in lines]
energized = set()
visited = set()

# 1 = right, 2 = left, 3 = up, 4 = down
nodes = [(0, 0, 1)]

while len(nodes) > 0:
    node = nodes.pop()
    (node_y, node_x, node_dir) = node

    if node_y < 0 or node_y >= len(grid) or node_x < 0 or node_x >= len(grid[0]) or node in visited:
        continue

    energized.add((node_y, node_x))
    visited.add(node)

    # 1 = right, 2 = left, 3 = up, 4 = down
    if grid[node_y][node_x] == '|':
        if node_dir == 1 or node_dir == 2:
            nodes.append((node_y + 1, node_x, 4))
            nodes.append((node_y - 1, node_x, 3))
        else:
            if node_dir == 3:
                nodes.append((node_y - 1, node_x, 3))
            else:
                nodes.append((node_y + 1, node_x, 4))
    elif grid[node_y][node_x] == '-':
        if node_dir == 3 or node_dir == 4:
            nodes.append((node_y, node_x + 1, 1))
            nodes.append((node_y, node_x - 1, 2))
        else:
            if node_dir == 2:
                nodes.append((node_y, node_x - 1, node_dir))
            else:
                nodes.append((node_y, node_x + 1, node_dir))
    elif grid[node_y][node_x] == '.':
        if node_dir == 1:
            nodes.append((node_y, node_x + 1, node_dir))
        elif node_dir == 2:
            nodes.append((node_y, node_x - 1, node_dir))
        elif node_dir == 3:
            nodes.append((node_y - 1, node_x, node_dir))
        elif node_dir == 4:
            nodes.append((node_y + 1, node_x, node_dir))
    elif grid[node_y][node_x] == '\\':
        # 1 = right, 2 = left, 3 = up, 4 = down
        if node_dir == 1:
            nodes.append((node_y + 1, node_x, 4))
        elif node_dir == 2:
            nodes.append((node_y - 1, node_x, 3))
        elif node_dir == 3:
            nodes.append((node_y, node_x - 1, 2))
        elif node_dir == 4:
            nodes.append((node_y, node_x + 1, 1))
    elif grid[node_y][node_x] == '/':
        # 1 = right, 2 = left, 3 = up, 4 = down
        if node_dir == 1:
            nodes.append((node_y - 1, node_x, 3))
        elif node_dir == 2:
            nodes.append((node_y + 1, node_x, 4))
        elif node_dir == 3:
            nodes.append((node_y, node_x + 1, 1))
        elif node_dir == 4:
            nodes.append((node_y, node_x - 1, 2))
    else:
        assert False

#for i, r in enumerate(grid):
#    for j, c in enumerate(r):
#        if (i, j) in energized:
#            print("#", end='')
#        else:
#            print(c, end='')
#    print()

print(len(energized))
