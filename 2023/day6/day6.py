import sys

input_file = "input"
if len(sys.argv) > 1:
    input_file = "input_%s" % sys.argv[1]

input = open(input_file).read()
lines = []
for line in input.split('\n'):
    if line:
        lines.append(line)

resulta = 1
resultb = 1

line = lines[0][10:]

times = []

for split in line.split(" "):
    if split:
        times.append(int(split))

time = 0
for i in range(0, len(line)):
    if line[i] >= '0' and line[i] <= '9':
        time *= 10
        time += int(line[i])

line = lines[1][10:]

distances = []

for split in line.split(" "):
    if split:
        distances.append(int(split))

distance = 0
for i in range(0, len(line)):
    if line[i] >= '0' and line[i] <= '9':
        distance *= 10
        distance += int(line[i])

for i in range(0, len(times)):
    ways = 0
    for j in range(1, times[i]):
        totalDistance = (times[i] - j + 1) * j - j

        if totalDistance > distances[i]:
            ways += 1

    resulta *= ways

ways = 0
for j in range(1, time):
    totalDistance = (time - j + 1) * j - j

    if totalDistance > distance:
        ways += 1

resultb = ways

print("A: " + str(resulta))
print("B: " + str(resultb))
