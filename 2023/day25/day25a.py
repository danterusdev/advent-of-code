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

import networkx as nx
G = nx.DiGraph()

for main, others in C.items():
    for other in others:
        G.add_edge(main, other, capacity=1.0)

source = list(C.keys())[0]
for dest in C.keys():
    if source != dest:
        value, (A, B) = nx.minimum_cut(G, source, dest)
        if value == 3:
            print(len(A) * len(B))
            exit(0)
