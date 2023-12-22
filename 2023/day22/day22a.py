import sys

import heapq

input = open(sys.argv[1]).read()
lines = input.strip().split("\n")

id_count = 0
bricks = []
for line in lines:
    end1, end2 = line.split("~")
    end1 = [int(x) for x in end1.split(",")]
    end2 = [int(x) for x in end2.split(",")]
    heapq.heappush(bricks, (min(end1[2], end2[2]), end1, end2, id_count))
    id_count += 1

can_be_removed = set()
for i in range(id_count):
    can_be_removed.add(i)

supporters_map = {}
settled_bricks = set()
while bricks:
    _, end1, end2, id = heapq.heappop(bricks)

    supporters = set()
    stopped = False
    while not stopped:
        end1[2] -= 1
        end2[2] -= 1

        if end1[2] == 0:
            stopped = True
            continue

        for brick in settled_bricks:
            if not (end2[0] >= brick[0][0] and end1[0] <= brick[1][0]):
                continue
            if not (end2[1] >= brick[0][1] and end1[1] <= brick[1][1]):
                continue
            if not (end2[2] >= brick[0][2] and end1[2] <= brick[1][2]):
                continue

            supporters.add(brick[2])
            stopped = True

    end1[2] += 1
    end2[2] += 1

    settled_bricks.add((tuple(end1), tuple(end2), id))
    supporters_map[id] = supporters

    if len(supporters) == 1:
        popped = set(supporters).pop()
        if popped in can_be_removed:
            can_be_removed.remove(popped)

print(len(can_be_removed))
