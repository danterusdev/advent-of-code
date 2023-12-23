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

D = {}
current = []
def f(r, c):
    if (r, c) in current:
        return -1

    current.append((r, c))

    if (r, c) == end:
        return 0

    max_dist = -1
    for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
        if not (0 <= nr < R and 0 <= nc < C):
            continue
        if G[nr][nc] == '#':
            continue

        if G[nr][nc] == '>' and not nc > c:
            continue
        if G[nr][nc] == 'v' and not nr > r:
            continue
        if G[nr][nc] == '<' and not nc < c:
            continue
        if G[nr][nc] == '^' and not nr < r:
            continue

        max_dist = max(max_dist, f(nr, nc))

    current.pop()

    if max_dist == -1:
        return -1

    if (r, c) not in D or 1 + max_dist > D[(r, c)]:
        D[(r, c)] = 1 + max_dist

    return 1 + max_dist

print(f(start[0], start[1]))

#for r in range(R):
#    for c in range(C):
#        if (r, c) in D:
#            print(f"{D[(r, c)]:03} ", end='')
#        else:
#            print("--- ", end='')
#    print()
