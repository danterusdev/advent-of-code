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
        return 1
    elif char == 'T':
        return 10
    elif char == 'A':
        return 14
    else:
        return int(char)

results = []

maxhandp = 0
for line in lines:
    cards, bid = line.split(" ")

    cards = [char for char in cards]
    cards = [toIndex(char) for char in cards]

    cardCounts = [0] * 15

    jokerCount = 0

    handPower = 0
    i = 15 * 15 * 15 * 15
    for card in cards:
        handPower += card * i
        cardCounts[card] += 1
        i /= 15

        if card == 1:
            jokerCount += 1

    maxhandp = max(maxhandp, handPower)

    found2 = 15
    found3 = 15

    ranking = 0
    for i, count in enumerate(cardCounts):
        if i == 1:
            count = 0

        if count + jokerCount >= 5:
            ranking = max(8000000 + handPower, ranking)

        if count + jokerCount >= 4:
            ranking = max(7000000 + handPower, ranking)

        if count + jokerCount >= 3:
            if found2 < 15 and count + jokerCount - found2 >= 3:
                ranking = max(6000000 + handPower, ranking)
            else:
                ranking = max(5000000 + handPower, ranking)

        if count + jokerCount >= 2:
            if found3 < 15 and count + jokerCount - found3 >= 2:
                ranking = max(6000000 + handPower, ranking)
            elif found2 < 15 and count + jokerCount - found2 >= 2:
                ranking = max(4000000 + handPower, ranking)
            else:
                ranking = max(3000000 + handPower, ranking)

        if count + jokerCount >= 1:
            ranking = max(ranking, 2000000 + handPower)

        if count + jokerCount >= 3:
            found3 = min(3 - count, found3)

        if count + jokerCount >= 2:
            found2 = min(2 - count, found2)

    results.append((ranking, int(bid)))

results.sort()

answer = 0

i = 1
for result in results:
    answer += result[1] * i
    i += 1

print(answer)
