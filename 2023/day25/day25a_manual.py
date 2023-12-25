import sys

input = open(sys.argv[1]).read()
L = input.strip().split("\n")

C = {}
for line in L:
    base, others = line.split(":")
    others = [x for x in others.strip().split()]

    if base not in C:
        C[base] = []

    C[base].extend(others)

    for other in others:
        if other not in C:
            C[other] = []

        C[other].append(base)

def f(cut_connections):
    counts = []
    for x in [cut_connections[0][0], cut_connections[0][1], cut_connections[1][0], cut_connections[1][1], cut_connections[2][0], cut_connections[2][1]]:
        seen = set()
        q = [x]
        while q:
            con = q.pop()
            if con in seen:
                continue

            seen.add(con)

            for connection in C[con]:
                if con == cut_connections[0][0] and connection == cut_connections[0][1]:
                    continue
                if connection == cut_connections[0][0] and con == cut_connections[0][1]:
                    continue
                if con == cut_connections[1][0] and connection == cut_connections[1][1]:
                    continue
                if connection == cut_connections[1][0] and con == cut_connections[1][1]:
                    continue
                if con == cut_connections[2][0] and connection == cut_connections[2][1]:
                    continue
                if connection == cut_connections[2][0] and con == cut_connections[2][1]:
                    continue

                q.append(connection)

        counts.append(len(seen))

    return counts

import heapq

def f3(node, target):
    seen = set()
    Q = []
    heapq.heappush(Q, (0, [node]))
    while Q:
        d, node = heapq.heappop(Q)

        if node[0] in seen:
            continue

        seen.add(node[0])

        if node[0] == target:
            return node

        for connection in C[node[0]]:
            new = [connection]
            new.extend(node)
            heapq.heappush(Q, (d + 1, new))

m = 0
connection_count = {}
for main in C:
    for other in C:
        m += 1
        results = f3(main, other)

        for i in range(len(results) - 1):
            first = results[i]
            second = results[i + 1]

            if first < second:
                key = (first, second)
            else:
                key = (second, first)

            if key in connection_count:
                connection_count[key] += 1
            else:
                connection_count[key] = 1

            if len(connection_count) <= 20:
                continue

            if m % 5000 == 0:
                thing = [(k, v) for k, v in sorted(connection_count.items(), key=lambda item: item[1])]
                if len(thing) > 3:
                    for i in range(len(thing) - 1, max(0, len(thing) - 10), -1):
                        for j in range(len(thing) - 2, max(0, len(thing) - 10), -1):
                            for k in range(len(thing) - 3, max(0, len(thing) - 10), -1):
                                current = [thing[i][0], thing[j][0], thing[k][0]]
                                result = f([current[0], current[1], current[2]])

                                for n in result:
                                    if n != len(C):
                                        first = result[0]
                                        i = 0
                                        while i < len(result):
                                            second = result[i]
                                            if second != first:
                                                break
                                            i += 1

                                        print(first * second)
                                        exit(0)
