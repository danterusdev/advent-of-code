import sys

input = open(sys.argv[1]).read()
L = input.strip().split("\n")

hails = []

for line in L:
    xs, vs = [x.strip() for x in line.split("@")]
    xs = [int(x) for x in xs.split(",")]
    vs = [int(x) for x in vs.split(",")]
    hails.append((xs, vs))

min = 200000000000000
max = 400000000000000

ans = 0
for i in range(0, len(hails)):
    hail1 = hails[i]
    for j in range(i + 1, len(hails)):
        hail2 = hails[j]

        a = hail1[0][0]
        b = hail1[1][0]
        c = hail1[0][1]
        d = hail1[1][1]

        e = hail2[0][0]
        f = hail2[1][0]
        g = hail2[0][1]
        h = hail2[1][1]
        if d / b - h / f == 0:
            pass
        else:
            x = (g - c - e * h / f + a * d / b) / (d / b - h / f)
            y = c + d / b * (x - a)

            if x >= min and x <= max and y >= min and y <= max and (bool(x > a) != bool(b <= 0)) and (bool(y > c) != bool(d < 0)) and (bool(x > e) != bool(f <= 0)) and (bool(y > g) != bool(h < 0)):
                ans += 1

print(ans)
