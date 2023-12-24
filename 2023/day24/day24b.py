import sys
import z3

input = open(sys.argv[1]).read()
L = input.strip().split("\n")

hails = []

for line in L:
    xs, vs = [x.strip() for x in line.split("@")]
    xs = [int(x) for x in xs.split(",")]
    vs = [int(x) for x in vs.split(",")]
    hails.append((xs, vs))

solve = z3.Solver()

x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')
vx = z3.Int('vx')
vy = z3.Int('vy')
vz = z3.Int('vz')
T = [z3.Int("T" + str(i)) for i in range(len(hails))]
ans = 0
for i in range(0, len(hails)):
    hail = hails[i]

    solve.add(x + T[i] * vx == hail[0][0] + T[i] * hail[1][0])
    solve.add(y + T[i] * vy == hail[0][1] + T[i] * hail[1][1])
    solve.add(z + T[i] * vz == hail[0][2] + T[i] * hail[1][2])

solve.check()
model = solve.model()

print(model.eval(x + y + z))
