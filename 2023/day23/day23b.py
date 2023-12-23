import sys

input = open(sys.argv[1]).read()
L = input.strip().split("\n")
G = [[c for c in li] for li in L]
R = len(G)
C = len(G[0])

for c in range(C):
    if G[0][c] == '.':
        start = (0, c)
    if G[R - 1][c] == '.':
        end = (R - 1, c)

sys.setrecursionlimit(10000)

GP = {}
def f(cr, cc):
    if (cr, cc) in GP:
        return

    found = []
    SEEN = set()
    Q = [(cr, cc, 0)]
    while Q:
        r, c, d = Q.pop()
        SEEN.add((r, c))
        count = 0
        for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
            if not (0 <= nr < R and 0 <= nc < C):
                continue
            if G[nr][nc] == '#':
                continue

            if (nr, nc) in SEEN:
                continue

            Q.append((nr, nc, d + 1))
            count += 1

        if (count > 1 or (r, c) == end) and (r, c) != (cr, cc):
            found.append((r, c, d))

            for i in range(count):
                Q.pop()

            GP[(cr, cc)] = found
            f(r, c)

f(start[0], start[1])

current = []
currents = set()
def f2(r, c):
    if (r, c) == end:
        return 0

    current.append((r, c))
    currents.add((r, c))

    max_dist = -1
    for nr, nc, nd in GP[(r, c)]:
        if (nr, nc) in currents:
            continue

        result = f2(nr, nc)
        if result >= 0:
            max_dist = max(max_dist, result + nd)

    currents.remove(current.pop())

    if max_dist == -1:
        return -1

    return max_dist

print(f2(start[0], start[1]))
