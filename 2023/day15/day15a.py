import sys

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

result = 0
for part in line.split(","):
    result += hash(part)

print(result)
