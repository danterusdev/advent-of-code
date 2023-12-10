import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

map = []
for line in lines:
    map.append([x for x in line])

max = 9999999

dots = []

distances = []
for row in range(len(map)):
    temp = []
    for col in range(len(map[row])):
        temp.append(max)
        if map[row][col] == 'S':
            start = row, col
        elif map[row][col] == '.':
            dots.append((row, col))
    distances.append(temp)

nodes = [(start[0], start[1], 0)]
in_loop = set()

while len(nodes) > 0:
    node = nodes.pop()

    if node[0] >= 0 and node[0] < len(map) and node[1] >= 0 and node[1] < len(map[node[0]]):
        if node[2] < distances[node[0]][node[1]]:
            in_loop.add((node[0], node[1]))
            distances[node[0]][node[1]] = node[2]

            char = map[node[0]][node[1]]
            if char == '|':
                nodes.append((node[0] - 1, node[1], node[2] + 1))
                nodes.append((node[0] + 1, node[1], node[2] + 1))
            elif char == '-':
                nodes.append((node[0], node[1] - 1, node[2] + 1))
                nodes.append((node[0], node[1] + 1, node[2] + 1))
            elif char == 'L':
                nodes.append((node[0], node[1] + 1, node[2] + 1))
                nodes.append((node[0] - 1, node[1], node[2] + 1))
            elif char == 'J':
                nodes.append((node[0], node[1] - 1, node[2] + 1))
                nodes.append((node[0] - 1, node[1], node[2] + 1))
            elif char == '7':
                nodes.append((node[0], node[1] - 1, node[2] + 1))
                nodes.append((node[0] + 1, node[1], node[2] + 1))
            elif char == 'F':
                nodes.append((node[0], node[1] + 1, node[2] + 1))
                nodes.append((node[0] + 1, node[1], node[2] + 1))
            elif char == 'S':
                right = map[node[0]][node[1] + 1]
                if right == '-' or right == '7' or right == 'J':
                    nodes.append((node[0], node[1] + 1, node[2] + 1))

                left = map[node[0]][node[1] - 1]
                if left == '-' or left == 'F' or left == 'L':
                    nodes.append((node[0], node[1] - 1, node[2] + 1))

                top = map[node[0] - 1][node[1]]
                if top == '|' or top == 'F' or top == '7':
                    nodes.append((node[0] - 1, node[1], node[2] + 1))

                bottom = map[node[0] + 1][node[1]]
                if bottom == '|' or bottom == 'J' or bottom == 'L':
                    nodes.append((node[0] + 1, node[1], node[2] + 1))
            else:
                assert False

maxdistance = 0
for array in distances:
    for distance in array:
        if distance < max and distance > maxdistance:
            maxdistance = distance

print(maxdistance)

for row in range(len(map) + 1):
    for col in range(len(map[0]) + 1):
        if (row == 0 or row == len(map) - 1) or (col == 0 or col == len(map[0]) - 1):
            if not (row, col) in in_loop:
                nodes.append((row, col))

visited = set()

while len(nodes) > 0:
    node = nodes.pop()

    if node not in visited:
        visited.add(node)

        nodex = node[1]
        nodey = node[0]

        if nodey < len(map) and nodex > 0:
            leftchar = map[nodey][nodex - 1]
            if ((nodey, nodex - 1) not in in_loop) or leftchar == '.' or leftchar == '-' or leftchar == '7' or leftchar == 'F':
                nodes.append((nodey, nodex - 1))

        if nodey < len(map) and nodex < len(map):
            rightchar = map[nodey][nodex]
            if ((nodey, nodex) not in in_loop) or rightchar == '.' or rightchar == '-' or rightchar == '7' or rightchar == 'F':
                nodes.append((nodey, nodex + 1))

        if nodex < len(map[0]) and nodey > 0:
            topchar = map[nodey - 1][nodex]
            if ((nodey - 1, nodex) not in in_loop) or topchar == '.' or topchar == '|' or topchar == 'L' or topchar == 'F':
                nodes.append((nodey - 1, nodex))

        if nodex < len(map[0]) and nodey < len(map):
            bottomchar = map[nodey][nodex]
            if ((nodey, nodex) not in in_loop) or bottomchar == '.' or bottomchar == '|' or bottomchar == 'L' or bottomchar == 'F':
                nodes.append((nodey + 1, nodex))

count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if (i, j) not in visited and (i, j) not in in_loop:
            count += 1

print(count)
