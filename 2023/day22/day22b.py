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

cannot_be_removed = set()

supporters_map = {}
settled_bricks = set()
brick_states = {}
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
    brick_states[id] = (tuple(end1), tuple(end2))
    supporters_map[id] = supporters

    if len(supporters) == 1:
        popped = set(supporters).pop()
        cannot_be_removed.add(popped)
        if popped in can_be_removed:
            can_be_removed.remove(popped)

ans = 0
for i in range(id_count):
    can_remove = True
    for brick in settled_bricks:
        for other_brick, value in supporters_map.items():
            if len(value) == 1 and i in value:
                can_remove = False

    if can_remove:
        ans += 1

ans = 0
for cannot in cannot_be_removed:
    valid_bricks = set()
    for i in range(id_count):
        valid_bricks.add(i)

    valid_bricks.remove(cannot)

    running = True
    while running:
        running = False
        for brick in range(id_count):
            if brick not in valid_bricks:
                continue

            any_support = brick_states[brick][0][2] == 1
            for supporter in supporters_map[brick]:
                if supporter in valid_bricks:
                    any_support = True

            if not any_support:
                valid_bricks.remove(brick)
                running = True
            else:
                brick += 1

    ans += id_count - len(valid_bricks) - 1

print(ans)
