import sys
import os

sys.path.insert(0, '.')
from lib import lines

input_file = "%s/input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    input_file = "%s/input_test"

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
input = open(input_file % script_directory).read()

resulta = 0
resultb = 0

thislines = lines(input)

seeds = [int(x) for x in thislines[0].split(":")[1][1:].split(" ")]

maps = []

j = 0
i = 1
while i < len(thislines):
    i += 1

    name = thislines[i]
    i += 1

    map = []

    while i < len(thislines) and thislines[i]:
        dst, src, range_ = [int(x) for x in thislines[i].split(" ")]
        map.append((src, dst, range_))
        i += 1

    j += 1
    maps.append(map)

resulta = 9999999999

for seed in seeds:
    value = seed
    for map in maps:
        for thing in map:
            if value >= thing[0] and value < thing[0] + thing[2]:
                value = value - thing[0] + thing[1]
                break

    if value < resulta:
        resulta = value

seedsfirst = [int(x) for x in thislines[0].split(":")[1][1:].split(" ")]
seeds = []
names = []

for i in range(0, len(seedsfirst), 2):
    seeds.append((seedsfirst[i], seedsfirst[i + 1]))

maps = []

j = 0
i = 1
while i < len(thislines):
    i += 1

    name = thislines[i]
    names.append(name)
    i += 1

    map = []

    while i < len(thislines) and thislines[i]:
        dst, src, range_ = [int(x) for x in thislines[i].split(" ")]
        map.append((src, dst, range_))
        i += 1

    j += 1
    maps.append(map)

resultb = 9999999999

for seed in seeds:
    seedranges = [seed]
    m = 0
    for map in maps:
        m += 1
        seedrangesnew = []
        p = 0
        while p < len(seedranges):
            seedrange = seedranges[p]
            dones = False
            leftover = [seedrange]
            for mapped in map:
                if mapped[0] < seedrange[0] + seedrange[1] and mapped[0] + mapped[2] > seedrange[0]:
                    foo = min(min(mapped[0] + mapped[2], seedrange[0] + seedrange[1]) - mapped[0], seedrange[1])
                    seedrangesnew.append((max(seedrange[0], mapped[0]) - mapped[0] + mapped[1], foo))
                    matched2 = (max(seedrange[0], mapped[0]), foo)

                    leftover.remove(seedrange)
                    if matched2[0] > seedrange[0]:
                        leftover.append((seedrange[0], matched2[0] - seedrange[0]))

                    if matched2[0] + matched2[1] < seedrange[0] + seedrange[1]:
                        leftover.append((matched2[0] + matched2[1], seedrange[0] + seedrange[1] - matched2[0] - matched2[1]))

                    dones = True
                    break

            if not dones:
                for range_ in leftover:
                    seedrangesnew.append(range_)
            else:
                for range_ in leftover:
                    seedranges.append(range_)

            p += 1

        seedranges = seedrangesnew

    for value in seedranges:
        if value[0] < resultb:
            resultb = value[0]

print("A: " + str(resulta))
print("B: " + str(resultb))
