import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

result = 0
for line in lines:
    data, backup = line.split()
    counts = [int(x) for x in backup.split(",")]

    data = [x for x in data]

    question_marks = []
    for i, x in enumerate(data):
        if x == '?':
            question_marks.append(i)

    localcount = 0
    for i in range(0, 2 ** len(question_marks)):
        states = [0] * len(question_marks)
        for j in range(len(states)):
            states[j] = True if ((i >> (len(states) - j - 1)) % 2) == 1 else False

        for j, mark in enumerate(question_marks):
            data[mark] = '.' if states[j] else '#'

        valid = True
        count = 0
        k = 0
        for j in range(len(data)):
            if data[j] == '#':
                count += 1
            elif data[j] == '.':
                if count > 0:
                    if k >= len(counts) or count != counts[k]:
                        valid = False
                        break
                    k += 1

                count = 0

        if count > 0:
            if k != len(counts) - 1 or count != counts[k]:
                valid = False
            k += 1

        if k != len(counts):
            valid = False

        if valid:
            localcount += 1
    result += localcount

print(result)
