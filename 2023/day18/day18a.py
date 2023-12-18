import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split("\n")]
points = []

minx = 9999
miny = 9999
maxx = -9999
maxy = -9999
x = 0
y = 0
prevdir = 'A'
insides = []
for line in lines:
    dir, dist, col = line.split()
    dist = int(dist)

    points.append((x, y))

    if dir == "D" and prevdir == "R":
        insides.append((y + 1, x - 1))

    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

    if dir == "R":
        x += dist
    elif dir == "L":
        x -= dist
    elif dir == "U":
        y -= dist
    elif dir == "D":
        y += dist
    else:
        assert False

    prevdir = dir

points.append((x, y))

cgrid = [['.' for x in range(maxx - minx + 1)] for y in range(maxy - miny + 1)]
grid = [['.' for x in range(maxx - minx + 1)] for y in range(maxy - miny + 1)]
for i in range(len(points) - 1):
    point1 = points[i]
    point2 = points[i + 1]

    for j in range(point1[0], point2[0] + 1) if point2[0] > point1[0] else range(point2[0], point1[0] + 1):
        for k in range(point1[1], point2[1]) if point2[1] > point1[1] else range(point2[1], point1[1] + 1):
            grid[k - miny][j - minx] = '#'

    if point1[0] == point2[0]:
        for j in range(point1[1], point2[1]) if point2[1] > point1[1] else range(point2[1], point1[1]):
            cgrid[j][point1[0]] = '#'

nodes = []
for inside in insides:
    nodes.append((inside[0] - miny, inside[1] - minx))

while len(nodes) > 0:
    node = nodes.pop()
    nodey, nodex = node

    if 0 <= nodex < len(grid[0]) and 0 <= nodey < len(grid) and grid[nodey][nodex] == '.':
        grid[nodey][nodex] = '#'
        nodes.append((nodey + 1, nodex))
        nodes.append((nodey - 1, nodex))
        nodes.append((nodey, nodex + 1))
        nodes.append((nodey, nodex - 1))

ans = 0
for line in grid:
    for c in line:
        if c == '#':
            ans += 1

print(ans)
