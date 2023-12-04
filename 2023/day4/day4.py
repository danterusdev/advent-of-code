import sys
import os
import functools

sys.path.insert(0, '.')
from lib import lines

input_file = "%s/input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    input_file = "%s/input_test"

script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
input = open(input_file % script_directory).read()

resulta = 0
resultb = 0

cards = []

for line in lines(input):
    count = 0
    start, left = line.split(":")
    winning, yours = left.split("|")

    winninglist = []
    yourlist = []

    for num in winning.split(" "):
        if not num:
            continue
        num = int(num.strip())
        winninglist.append(num)

        for yournum in yours.split(" "):
            if not yournum:
                continue
            yournum = int(yournum.strip())
            if yournum == num:
                count += 1

            if yournum not in yourlist:
                yourlist.append(yournum)

    if count > 0:
        resulta += 2 ** (count - 1)

    cards.append((winninglist, yourlist))

@functools.cache
def f(card):
    total = 1
    i = 1
    for winning in cards[card][0]:
        for yours in cards[card][1]:
            if winning == yours:
                total += f(card + i)
                i += 1

    return total

for i in range(0, len(cards)):
    resultb += f(i)

print("A: " + str(resulta))
print("B: " + str(resultb))
