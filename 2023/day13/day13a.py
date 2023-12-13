import sys

input = open(sys.argv[1]).read()
patterns = [x for x in input.strip().split('\n\n')]

result = 0

for pattern in patterns:
    grid = [[x for x in p] for p in pattern.split('\n')]

    found = False
    patternx = 0
    patternxsize = 0
    for col in range(0, len(grid[0]) - 1):
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
                        #print('a', left, right)
                        matches = False

            if matches:
                size += 1

            left -= 1
            right += 1

        #print(col, size)
        max_size = min(len(grid[0]) - col - 1, col + 1)
        if size == max_size and size > patternxsize:
            patternx = col + 1
            patternxsize = size
            found = True

    if found:
        result += patternx

    found = False
    patterny = 0
    patternysize = 0
    for row in range(0, len(grid) - 1):
        size = 0
        top = row
        bottom = row + 1

        matches = True
        while matches:
            matches = True

            if top < 0 or bottom >= len(grid):
                matches = False
            else:
                matches = grid[top] == grid[bottom]

            if matches:
                size += 1

            top -= 1
            bottom += 1

        max_size = min(len(grid) - row - 1, row + 1)
        if size == max_size and size > patternysize:
            patterny = row + 1
            patternysize = size
            found = True

    #print(found)
    if found:
        result += patterny * 100

print(result)
