import sys

input = open(sys.argv[1]).read()
grid = [[char for char in line] for line in input.strip().split('\n')]

cache = {}

stopping_points = set()
rocks = set()
for col in range(len(grid[0])):
    for row in range(len(grid)):
        if grid[row][col] == '#':
            stopping_points.add((row, col))
        elif grid[row][col] == 'O':
            rocks.add((row, col))

results = {}
ids = []

pattern = []

computed = False
for i in range(0, 1000000000):
    id = 37
    for r in rocks:
        id += r[0] * 4325 + r[1]

    if id in cache:
        pattern = ids[len(cache[id]):]
        break

    visited = set()
    for k in range(len(grid)):
        for r in set(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_row != k or r in visited:
                continue

            sp = -1
            for stopping_point in range(0, r_row):
                if (stopping_point, r_col) in stopping_points or (stopping_point, r_col) in rocks:
                    sp = max(sp, stopping_point)

            rocks.remove(r)
            new_pos = (sp + 1, r_col)
            rocks.add(new_pos)
            visited.add(new_pos)

    visited = set()
    for k in range(len(grid[0])):
        for r in set(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_col != k or r in visited:
                continue

            sp = -1
            for stopping_point in range(0, r_col):
                if (r_row, stopping_point) in stopping_points or (r_row, stopping_point) in rocks:
                    sp = max(sp, stopping_point)

            rocks.remove(r)
            new_pos = (r_row, sp + 1)
            rocks.add(new_pos)
            visited.add(new_pos)

    visited = set()
    for k in range(len(grid) - 1, -1, -1):
        for r in set(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_row != k or r in visited:
                continue

            sp = len(grid)
            for stopping_point in range(r_row + 1, len(grid)):
                if (stopping_point, r_col) in stopping_points or (stopping_point, r_col) in rocks:
                    sp = min(sp, stopping_point)

            rocks.remove(r)
            new_pos = (sp - 1, r_col)
            rocks.add(new_pos)
            visited.add(new_pos)

    visited = set()
    for k in range(len(grid[0]) - 1, -1, -1):
        for r in set(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_col != k or r in visited:
                continue

            sp = len(grid[0])
            for stopping_point in range(r_col + 1, len(grid[0])):
                if (r_row, stopping_point) in stopping_points or (r_row, stopping_point) in rocks:
                    sp = min(sp, stopping_point)

            rocks.remove(r)
            new_pos = (r_row, sp - 1)
            rocks.add(new_pos)
            visited.add(new_pos)

    cache[id] = list(ids)

    result = 0
    for r in rocks:
        result += len(grid) - r[0]

    ids.append(id)
    results[id] = result
else:
    computed = True
    print(result)

if not computed:
    start_index = i
    print(results[pattern[(1000000000 - start_index - 1) % len(pattern)]])
