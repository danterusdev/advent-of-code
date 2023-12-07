import sys

input_file = "input"
if len(sys.argv) > 1:
    input_file = "input_%s" % sys.argv[1]

input = open(input_file).read()
lines = [x for x in input.strip().split('\n')]

priority = []

def toIndex(char):
    if char == 'K':
        return 13
    elif char == 'Q':
        return 12
    elif char == 'J':
        return 11
    elif char == 'T':
        return 10
    elif char == 'A':
        return 14
    else:
        return int(char)

results = []

for line in lines:
    cards, bid = line.split(" ")

    cards = [char for char in cards]
    cards = [toIndex(char) for char in cards]

    cardCounts = [0] * 15

    handPower = 0
    i = 15 * 15 * 15 * 15
    for card in cards:
        handPower += card * i
        cardCounts[card] += 1
        i /= 15

    found2 = False
    found3 = False

    ranking = 0
    for i, count in enumerate(cardCounts[::-1]):
        if count == 5:
            ranking = max(8000000 + handPower, ranking)
        elif count == 4:
            ranking = max(7000000 + handPower, ranking)
        elif count == 3:
            if found2:
                ranking = max(6000000 + handPower, ranking)
            else:
                ranking = max(5000000 + handPower, ranking)

            found3 = True
        elif count == 2:
            if found3:
                ranking = max(6000000 + handPower, ranking)
            elif found2:
                ranking = max(4000000 + handPower, ranking)
            else:
                ranking = max(3000000 + handPower, ranking)

            found2 = True
        elif count == 1:
            ranking = max(ranking, 2000000 + handPower)

    results.append((ranking, int(bid)))

results.sort()

answer = 0

i = 1
for result in results:
    answer += result[1] * i
    i += 1

print(answer)
