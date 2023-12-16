import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split("\n")]
grid = [[c for c in line] for line in lines]

maxenergized = 0

# 1 = right, 2 = left, 3 = up, 4 = down
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not (i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1):
            continue

        dirs = []

        if i == 0:
            dirs.append(4)

        if j == 0:
            dirs.append(1)

        if i == len(grid) - 1:
            dirs.append(3)

        if j == len(grid[0]) - 1:
            dirs.append(2)

        for dir in dirs:
            energized = set()
            visited = set()
            nodes = [(i, j, dir)]

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

            if len(energized) > maxenergized:
                maxenergized = len(energized)

print(maxenergized)
