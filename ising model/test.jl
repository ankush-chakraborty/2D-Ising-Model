using Plots
using LinearAlgebra
using Random

i_prev(i) = i == 1 ? N : i - 1
i_next(i) = i == N ? 1 : i + 1
j_prev(j) = j == 1 ? N : j - 1
j_next(j) = j == N ? 1 : j + 1

function H(s)
    J = 1
    N = size(s, 1)
    sum = 0
    for i in 1:N
        for j in 1:N
            sum += s[i, j] * (s[i_prev(i), j] + s[i_next(i), j] + s[i, j_prev(j)] + s[i, j_next(j)])
        end
    end
    H = -J/2*sum
    return H
end

print("check")
function move(s, beta)
    J = 1
    N = size(s, 1)
    E = H(s)
    i, j = rand(1:N), rand(1:N)
    dE = J * s[i, j] * (s[i_prev(i), j] + s[i_next(i), j] + s[i, j_prev(j)] + s[i, j_next(j)])

    if dE < 0
        s[i, j] *= -1
        E += dE
    elseif rand() < exp(-beta*dE)
        s[i, j] *= -1
        E += dE
    end

    return s
end
print("check")
function M(s)
    N = size(s, 1)
    return sum(s)/N^2
end
print("check")
N = 30
mcmoves = 5000
state = ones(N, N)

x = 0.01:0.01:3
m = []
e = []
for i in x
    s = copy(state)
    beta = 1/i
    for j in 1:mcmoves
        s = move(s, beta)
    end
    print("checkpoint", i)
    append!(m, abs(M(s)))
    append!(e, H(s))
end

c = []
for i in 1:(length(x) - 1)
    append!(c, (e[i+1] - e[i])/0.01)
end

display(plot(x, m))
display(plot(x, e))