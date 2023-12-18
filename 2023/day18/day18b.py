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
    dir, dist, code = line.split()
    code = code[2:-1]
    dist = int(code[:-1], 16)
    dir = int(code[-1])

    points.append((x, y))

    # 0 means R, 1 means D, 2 means L, and 3 means U.

    minx = min(minx, x)
    maxx = max(maxx, x)
    miny = min(miny, y)
    maxy = max(maxy, y)

    if dir == 0:
        x += dist
    elif dir == 2:
        x -= dist
    elif dir == 3:
        y -= dist
    elif dir == 1:
        y += dist
    else:
        assert False

    prevdir = dir

points.append((x, y))

vertlines = []
horlines = []
for i in range(len(points) - 1):
    point1 = points[i]
    point2 = points[i + 1]

    if point1[0] == point2[0]:
        if point1[1] < point2[1]:
            vertlines.append((point1[0], point1[1] - miny, point2[1] - point1[1]))
        else:
            vertlines.append((point1[0], point2[1] - miny, point1[1] - point2[1]))
    else:
        is_different = False
        if i == 0:
            if abs(points[i - 2][1] - points[i + 2][1]) > max(abs(points[i - 2][1] - point1[1]), abs(points[i + 2][1] - point1[1])):
                is_different = True
        else:
            if abs(points[i - 1][1] - points[i + 2][1]) > max(abs(points[i - 1][1] - point1[1]), abs(points[i + 2][1] - point1[1])):
                is_different = True

        horlines.append((min(point1[0], point2[0]), point1[1] - miny, max(point1[0], point2[0]) - min(point1[0], point2[0]), is_different))

rows = [[] for x in range(maxy - miny + 1)]

for line in vertlines:
    x, y, height = line

    for i in range(y + 1, y + height):
        rows[i].append((x, 1, True))

for line in horlines:
    x, y, width, different = line

    rows[y].append((x, width + 1, different))

for row in rows:
    row.sort()

override = False
ans = 0
for j, row in enumerate(rows):
    i = 0
    while i < len(row):
        first = row[i]
        i += 1
        if first[2] or override:
            override = False
            second = row[i]

            if second[2]:
                ans += second[0] - (first[0] + first[1])
                ans += second[1]
                i += 1
            else:
                ans += second[0] - (first[0] + first[1])
                override = True

            ans += first[1]
        else:
            ans += first[1]

print(ans)
