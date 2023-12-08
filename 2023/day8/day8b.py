import sys
import math

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

path_map = {}

for path in lines[2:]:
    path, outputs = path.split("=")
    path = path.strip()
    outputs = outputs.strip()[1:-1]
    outputleft, outputright = outputs.split(",")
    outputright = outputright.strip()

    path_map[path] = (outputleft, outputright)

currents = []
for input in path_map.keys():
    if input.endswith("A"):
        currents.append(input)

def allZ(currents):
    allZ = True
    for current in currents:
        if not current.endswith("Z"):
            allZ = False

    return allZ

stepcounts = []
steps = 0
count = 0
for current in currents:
    steps = 0
    done = False
    while not done:
        for instruction in lines[0]:
            if current.endswith("Z"):
                done = True
                break

            if instruction == 'L':
                current = path_map[current][0]
            else:
                current = path_map[current][1]

            steps += 1

    stepcounts.append(steps)

print(math.lcm(*stepcounts))
