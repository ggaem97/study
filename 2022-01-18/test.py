import sys
# input = sys.stdin.readline

sys.stdin = open('in2.txt', 'r')
n = int(input())
graph = [input().split() for _ in range(n)]
tmp = []
for i in range(n):
    tmp.append(graph[i])

dx = [1,0,-1,0]
dy = [0,-1,0,1]


def findStudent(i, j):
    for t in range(4):
        x = i
        y = j
        while 0 <= x + dx[t] < n and 0 <= y + dy[t] < n:
            x += dx[t]
            y += dy[t]
            if graph[x][y] == 'O':
                break
            if graph[x][y] == 'S':
                return True

    return False


def DFS(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    if findStudent(i, j):
                        return
        print('answer is True')
        for i in range(n):
            print(graph[i])

        print()
        result = True
        return

    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    count += 1
                    DFS(count)
                    graph[i][j] = 'X'
                    count -= 1

answer = False
DFS(0)
if answer:
    print('YES')
else:
    print('NO')