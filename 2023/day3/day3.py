import sys
import os

sys.path.insert(0, '.')
from lib import lines

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
input = open("%s/input" % script_directory).read()

resulta = 0
resultb = 0

nums = []
symbols = []

gears = []

j = 0
for line in lines(input):
    i = 0
    while i < len(line):
        if line[i] >= '0' and line[i] <= '9':
            num = 0
            k = 0
            while i < len(line) and line[i] >= '0' and line[i] <= '9':
                num = num * 10
                num = num + int(line[i])
                k += 1
                i += 1

            nums.append((num, i - k, j, k))  # x, y, length
        elif line[i] != '.':
            symbols.append((i, j))
            if line[i] == '*':
                gears.append((i, j))
            i += 1
        else:
            i += 1

    j += 1

for num in nums:
    for symbol in symbols:
        if symbol[0] >= num[1] - 1 and symbol[0] <= num[1] + num[3] and symbol[1] >= num[2] - 1 and symbol[1] <= num[2] + 1:
            resulta += num[0]
            break

for gear in gears:
    count = 0
    parts = []
    for num in nums:
        if gear[0] >= num[1] - 1 and gear[0] <= num[1] + num[3] and gear[1] >= num[2] - 1 and gear[1] <= num[2] + 1:
            parts.append(num[0])
            count += 1

    if count == 2:
        resultb += parts[0] * parts[1]

print("A: " + str(resulta))
print("B: " + str(resultb))
