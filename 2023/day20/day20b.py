import sys

from collections import deque
from math import lcm

input = open(sys.argv[1]).read()
lines = input.strip().split("\n")

module_states = []
module_infos = []
modules = {}
module_names = []

references = []

i = 0
for line in lines:
    name, results = line.split("->")

    name = name.strip()
    results = results.strip()

    if name[0] == '%':
        real_name = name[1:]
        a = []
        for x in results.split(','):
            a.append(x.strip())
            references.append((x.strip(), real_name))
        module_infos.append(("FF", a))
        module_states.append(False)
    elif name[0] == '&':
        real_name = name[1:]
        a = []
        for x in results.split(','):
            a.append(x.strip())
            references.append((x.strip(), real_name))
        module_infos.append(("CJ", a))
        module_states.append({})
    else:
        # broadcaster
        real_name = name
        a = []
        for x in results.split(','):
            a.append(x.strip())
            references.append((x.strip(), real_name))

        module_infos.append(("BC", a))
        module_states.append(0)

    modules[real_name] = i
    module_names.append(real_name)
    i += 1

second_layers = []
for i in references:
    if i[0] == "df":
        second_layers.append(i[1])

for key, value in modules.items():
    if module_infos[value][0] == "CJ":
        for i in references:
            if i[0] == key:
                module_states[value][i[1]] = False

cache = {}
first_runs = {}
for c in range(1, 10000):
    pulses = deque([(None, "broadcaster", 'L')])
    while len(pulses) > 0:
        pulse = pulses.popleft()
        if pulse[1] not in modules:
            continue
        i = modules[pulse[1]]

        name = module_names[i]
        if module_infos[i][0] == "BC":
            for x in module_infos[i][1]:
                pulses.append((name, x, pulse[2]))
        elif module_infos[i][0] == "CJ":
            prev_name = pulse[0]
            module_states[i][prev_name] = 'H' == pulse[2]

            sending_high = not all(value for key, value in module_states[i].items())
            if not sending_high:
                for x in module_infos[i][1]:
                    pulses.append((name, x, 'L'))
            else:
                for x in module_infos[i][1]:
                    pulses.append((name, x, 'H'))

            if name in second_layers and sending_high and name:
                first_runs[name] = c - cache.get(name, 0)
                cache[name] = c

        elif module_infos[i][0] == "FF":
            if pulse[2] == 'L':
                module_states[i] = not module_states[i]
                for x in module_infos[i][1]:
                    pulses.append((name, x, 'H' if module_states[i] else 'L'))
        else:
            assert False

print(lcm(*first_runs.values()))
