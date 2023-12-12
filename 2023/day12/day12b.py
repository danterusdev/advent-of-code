import sys
from functools import cache

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

result = 0
for line in lines:
    data, backup = line.split()
    counts = [int(x) for x in backup.split(",")]

    data = [x for x in data]
    data.append('?')
    data = data * 5
    data.pop()
    counts = counts * 5

    @cache
    def compute(i, count_index):
        if i >= len(data):
            return -1 if count_index < len(counts) else 0

        found = True
        if count_index >= len(counts):
            for j in range(i, len(data)):
                if data[j] == '#':
                    found = False

            return 0 if found else -1
        else:
            current_count = counts[count_index]

            for j in range(i, i + current_count):
                if j >= len(data) or data[j] == '.':
                    found = False
                    break

            if i + current_count < len(data) and data[i + current_count] == '#':
                found = False

            i_new = i
            if found:
                count_index += 1
                i_new += current_count + 1

            if not found:
                return -1

            any_valid = False
            j = 0
            if i_new >= len(data) and count_index == len(counts):
                any_valid = True
            else:
                for k in range(len(data) - i_new + 1):
                    can_do = True
                    for m in range(i_new, i_new + k):
                        if data[m] == '#':
                            can_do = False

                    if can_do:
                        computed = compute(i_new + k, count_index)
                        if computed >= 0:
                            j += computed
                            any_valid = True

            if any_valid:
                return max(j, 1)
            return -1

    j = 0
    for k in range(len(data)):
        can_do = True
        for m in range(0, k):
            if data[m] == '#':
                can_do = False

        if can_do:
            computed = compute(k, 0)
            if computed > 0:
                j += computed

    result += j

print(result)
