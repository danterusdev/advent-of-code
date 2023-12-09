import sys

input = open(sys.argv[1]).read()
lines = [x for x in input.strip().split('\n')]

histories = []

for line in lines:
    history = [int(x) for x in line.split()]
    histories.append(history)

def expand_history(history):
    result = []
    for i in range(len(history) - 1):
        result.append(history[i + 1] - history[i])
    return result

resulta = 0
resultb = 0

for history in histories:
    tree = [history]

    while not all(i == 0 for i in history):
        history = expand_history(history)
        tree.append(history)

    value_right = 0
    value_left = 0
    for i in range(len(tree) - 1):
        value_right = value_right + tree[len(tree) - i - 2][-1]
        value_left = tree[len(tree) - i - 2][0] - value_left

    resulta += value_right
    resultb += value_left

print(resulta)
print(resultb)
