import sys

input = open(sys.argv[1]).read()
grid = [[char for char in line] for line in input.strip().split('\n')]
print(grid)

stopping_points = []
rocks = []
for col in range(len(grid[0])):
    sp_in = []
    r_in = []

    for row in range(len(grid)):
        if grid[row][col] == '#':
            sp_in.append(row)
        elif grid[row][col] == 'O':
            r_in.append(row)

    stopping_points.append(sp_in)
    rocks.append(r_in)

result = 0
for i in range(len(rocks)):
    col_sp = stopping_points[i]
    col_r = rocks[i]

    for j, r in enumerate(col_r):
        sp = -1
        for stopping_point in range(r - 1, -1, -1):
            if stopping_point in col_sp or stopping_point in col_r:
                sp = stopping_point
                break

        col_r[j] = sp + 1
        result += len(grid) - sp - 1

print(result)
