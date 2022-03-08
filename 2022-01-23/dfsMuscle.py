import sys
sys.stdin = open('muscleDecrease.txt', 'r')
n, k = map(int, input().split())
weight = list(map(int, input().split()))
visited = [False]*(n)
power = 500
res = 0


def DFS(count):
    global power, res
    if count == n:
        res += 1
    else:
        for i in range(n):
            if not visited[i]:
                potential = weight[i] - k
                if power + potential >= 500:
                    visited[i] = True
                    power += potential
                    DFS(count+1)
                    power -= potential
                    visited[i] = False


DFS(0)
print(res)
