import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

instructions, blank, *paths = lines

path_map = {}

for path in paths:
    path, outputs = path.split("=")
    path = path.strip()
    outputs = outputs.strip()[1:-1]
    outputleft, outputright = outputs.split(",")
    outputright = outputright.strip()
    print(path)
    print(outputs)

    path_map[path] = (outputleft, outputright)

current = "AAA"
steps = 0
done = False
while not done:
    for instruction in instructions:
        if current == "ZZZ":
            done = True
            break

        if instruction == 'L':
            current = path_map[current][0]
        else:
            current = path_map[current][1]
        steps += 1

print(steps)
