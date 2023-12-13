import sys

input = open(sys.argv[1]).read()
patterns = [x for x in input.strip().split('\n\n')]

result = 0

for pattern in patterns:
    grid = [[x for x in p] for p in pattern.split('\n')]

    to_change = []
    change_for_horiz = False
    for col in range(0, len(grid[0]) - 1):
        differences = []
        size = 0
        left = col
        right = col + 1

        matches = True
        while matches:
            matches = True

            if left < 0 or right >= len(grid[0]):
                matches = False
            else:
                for row in range(len(grid)):
                    if grid[row][left] != grid[row][right]:
                        differences.append((row, left))

            if len(differences) <= 1 and matches:
                size += 1

            left -= 1
            right += 1

        max_size = min(len(grid[0]) - col - 1, col + 1)
        if size == max_size and len(differences) == 1:
            to_change.append(differences[0])
            change_for_horiz = False
            break

    for row in range(0, len(grid) - 1):
        differences = []
        size = 0
        top = row
        bottom = row + 1

        matches = True
        while matches:
            matches = True

            if top < 0 or bottom >= len(grid):
                matches = False
            else:
                for col in range(len(grid[0])):
                    if grid[top][col] != grid[bottom][col]:
                        differences.append((top, col))

            if len(differences) <= 1 and matches:
                size += 1

            top -= 1
            bottom += 1

        max_size = min(len(grid) - row - 1, row + 1)
        if size == max_size and len(differences) == 1:
            to_change.append(differences[0])
            change_for_horiz = True
            break

    to_change = to_change[0]
    if grid[to_change[0]][to_change[1]] == '#':
        grid[to_change[0]][to_change[1]] = '.'
    else:
        grid[to_change[0]][to_change[1]] = '#'

    found = False
    patternx = 0
    has_change = False
    for col in range(0, len(grid[0]) - 1):
        has_change = False
        size = 0
        left = col
        right = col + 1

        matches = True
        while matches:
            matches = True

            if left < 0 or right >= len(grid[0]):
                matches = False
            else:
                for row in range(len(grid)):
                    if (row, left) == to_change or (row, right) == to_change:
                        has_change = True

                    if grid[row][left] != grid[row][right]:
                        matches = False

            if matches:
                size += 1

            left -= 1
            right += 1

        max_size = min(len(grid[0]) - col - 1, col + 1)
        if size == max_size and has_change:
            patternx = col + 1
            found = True
            break

    if found and not change_for_horiz:
        result += patternx

    found = False
    patterny = 0
    has_change = False
    for row in range(0, len(grid) - 1):
        has_change = False
        size = 0
        top = row
        bottom = row + 1

        matches = True
        while matches:
            matches = True

            if top < 0 or bottom >= len(grid):
                matches = False
            else:
                if top == to_change[0] or bottom == to_change[0]:
                    has_change = True
                matches = grid[top] == grid[bottom]

            if matches:
                size += 1

            top -= 1
            bottom += 1

        max_size = min(len(grid) - row - 1, row + 1)
        if size == max_size and has_change:
            patterny = row + 1
            found = True
            break

    if found and change_for_horiz:
        result += patterny * 100

print(result)
