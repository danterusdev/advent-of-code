import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

initial_map = [[i for i in x] for x in lines]

empty_rows = set()
for i in range(len(initial_map)):
    if '#' not in initial_map[i]:
        empty_rows.add(i)

empty_columns = set()
for i in range(len(initial_map[0])):
    is_in = False
    for j in range(len(initial_map)):
        if initial_map[j][i] == '#':
            is_in = True

    if not is_in:
        empty_columns.add(i)

galaxy_locations = []
for i in range(len(initial_map)):
    for j in range(len(initial_map[i])):
        if initial_map[i][j] == '#':
            galaxy_locations.append((i, j))

for expand_distance in [2, 1000000]:
    result = 0
    for i in range(len(galaxy_locations)):
        for j in range(i + 1, len(galaxy_locations)):
            miny = min(galaxy_locations[i][0], galaxy_locations[j][0])
            maxy = max(galaxy_locations[i][0], galaxy_locations[j][0])
            minx = min(galaxy_locations[i][1], galaxy_locations[j][1])
            maxx = max(galaxy_locations[i][1], galaxy_locations[j][1])

            distance = 0
            for k in range(minx, maxx):
                if k in empty_columns:
                    distance += expand_distance
                else:
                    distance += 1

            for k in range(miny, maxy):
                if k in empty_rows:
                    distance += expand_distance
                else:
                    distance += 1

            result += distance

    print(result)
