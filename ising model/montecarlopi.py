from numpy import random as r

t = 2000
c = 0
rad = 1

for i in range(t):
    x = r.uniform(0, rad)
    y = r.uniform(0, rad)

    if x**2 + y**2 <= rad**2:
        c += 1

print(4*c/t)
