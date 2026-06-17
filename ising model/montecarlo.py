import numpy as np
import math
import matplotlib.pyplot as plt

def H(s):
    J = 1
    N = s.shape[0]
    sum = 0
    for i in range(N):
        for j in range(N):
            sum += s[i, j]*(s[(i-1)%N, j] + s[(i+1)%N, j] + s[i, (j-1)%N] + s[i, (j+1)%N])
    
    H = -J/2*sum
    return H

def move(s, beta):
    J = 1
    N = s.shape[0]
    E = H(s)
    a, b = np.random.randint(0, N), np.random.randint(0, N)
    dE = J*s[a, b]*(s[(a-1)%N, b] + s[(a+1)%N, b] + s[a, (b-1)%N] + s[a, (b+1)%N])
    if dE < 0:
        s[a, b] *= -1
        E += dE
    elif np.random.uniform(0, 1) < math.exp(-beta*dE):
        s[a, b] *= -1
        E += dE
    return s

def M(s):
    N = s.shape[0]
    return np.sum(s)/N**2

N = 30
mcmoves = 5000
state = np.zeros((N, N)) + 1

x = np.arange(0.01, 3, 0.01)
m = []
e = []
for i in x:
    s = state.copy()
    beta = 1/i
    for j in range(mcmoves):
        s = move(s, beta)
    
    print("checkpoint", i)
    m += [abs(M(s)),]
    e += [H(s),]

c = []
for i in range(len(e)-1):
    c += (e[i+1] - e[i])/0.01

c = np.array(c)
m = np.array(m)
e = np.array(e)
plt.plot(x, m)
plt.show()
plt.plot(x, e)
plt.show()
