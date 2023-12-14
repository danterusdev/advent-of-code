import sys

input = open(sys.argv[1]).read()
grid = [[char for char in line] for line in input.strip().split('\n')]

cache = {}

stopping_points = []
rocks = []
for col in range(len(grid[0])):
    for row in range(len(grid)):
        if grid[row][col] == '#':
            stopping_points.append((row, col))
        elif grid[row][col] == 'O':
            rocks.append((row, col))

results = {}
ids = []

duplicates = {}

pattern = []

for i in range(0, 1000000000):
    id = 37
    for r in rocks:
        id += r[0] * 4325 + r[1]

    if id in cache:
        pattern = ids[len(cache[id]):]
        break

    visited = set()
    for k in range(len(grid)):
        for j, r in enumerate(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_row != k or r in visited:
                continue

            sp = -1
            for stopping_point in range(0, r_row):
                if (stopping_point, r_col) in stopping_points or (stopping_point, r_col) in rocks:
                    sp = max(sp, stopping_point)

            rocks[j] = (sp + 1, r_col)
            visited.add(rocks[j])

    visited = set()
    for k in range(len(grid[0])):
        for j, r in enumerate(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_col != k or r in visited:
                continue

            sp = -1
            for stopping_point in range(0, r_col):
                if (r_row, stopping_point) in stopping_points or (r_row, stopping_point) in rocks:
                    sp = max(sp, stopping_point)

            rocks[j] = (r_row, sp + 1)
            visited.add(rocks[j])

    visited = set()
    for k in range(len(grid) - 1, -1, -1):
        for j, r in enumerate(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_row != k or r in visited:
                continue

            sp = len(grid)
            for stopping_point in range(r_row + 1, len(grid)):
                if (stopping_point, r_col) in stopping_points or (stopping_point, r_col) in rocks:
                    sp = min(sp, stopping_point)

            rocks[j] = (sp - 1, r_col)
            visited.add(rocks[j])

    visited = set()
    for k in range(len(grid[0]) - 1, -1, -1):
        for j, r in enumerate(rocks):
            r_row = r[0]
            r_col = r[1]

            if r_col != k or r in visited:
                continue

            sp = len(grid[0])
            for stopping_point in range(r_col + 1, len(grid[0])):
                if (r_row, stopping_point) in stopping_points or (r_row, stopping_point) in rocks:
                    sp = min(sp, stopping_point)

            rocks[j] = (r_row, sp - 1)
            visited.add(rocks[j])

    cache[id] = list(ids)

    result = 0
    for r in rocks:
        result += len(grid) - r[0]

    ids.append(id)
    results[id] = result
    print(result)

start_index = i
print(results[pattern[(1000000000 - start_index - 1) % len(pattern)]])
