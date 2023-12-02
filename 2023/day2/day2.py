import sys

part = sys.argv[1][0]

input = open("day2/input")
lines = input.read().split("\n")

result = 0

for line in lines:
    if not line:
        continue

    if part == 'a':
        max_red = 12
        max_green = 13
        max_blue = 14
    else:
        max_red = 0
        max_green = 0
        max_blue = 0

    game_valid = True

    small_line = line[line.index(":") + 1:]
    split = small_line.split(";")
    for thing in split:
        split2 = thing.split(",")
        for thing2 in split2:
            thing2 = thing2.strip()

            split3 = thing2.split(" ")
            count = int(split3[0])

            if split3[1] == "red":
                if count > max_red:
                    if part == 'a':
                        game_valid = False
                    else:
                        max_red = count
            if split3[1] == "green":
                if count > max_green:
                    if part == 'a':
                        game_valid = False
                    else:
                        max_green = count
            if split3[1] == "blue":
                if count > max_blue:
                    if part == 'a':
                        game_valid = False
                    else:
                        max_blue = count
    if part == 'a':
        if game_valid:
            id = int(line[line.index(" ") + 1 : line.index(":")])
            result += id
    else:
        result += max_red * max_green * max_blue

print(result)
