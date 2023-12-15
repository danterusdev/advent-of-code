import sys
from collections import OrderedDict

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split("\n")]
line = lines[0]

def hash(string):
    value = 0
    for c in string:
        value += ord(c)
        value *= 17
        value %= 256

    return value

box = [OrderedDict() for x in range(256)]

for part in line.split(","):
    if part[len(part) - 2] == '=':
        label = part[0:len(part) - 2]
        box[hash(label)][label] = int(part[len(part) - 1])
    else:
        label = part[0:len(part) - 1]
        if label in box[hash(label)]:
            del box[hash(label)][label]

result = 0
for i, box2 in enumerate(box):
    for j, (key, lens) in enumerate(box2.items()):
        result += (1 + i) * (j + 1) * lens

print(result)
