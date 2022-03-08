n, m, v = map(int, input().split())
n += 1
E = [[0]*n for _ in ' '*n]
for _ in ' '*m:a, b = map(int, input().split());E[a][b] = E[b][a] = 1
S, V = [], [0]*n

def D(i):
    S.append(i)
    V[i] = 1
    for j in range(n):
        if E[i][j] and not V[j]:
            D(j)

D(v)
print(*S)
Q, V = [v], [0]*n
V[v] = 1
for i in Q:
    for j in range(n):
        if E[i][j] and not V[j]:
            Q += [j]
            V[j] = 1
print(*Q)