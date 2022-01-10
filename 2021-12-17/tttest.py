computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
graph = [[]]
visited = [False]*4

def dfs(x):
    global cnt
    cnt +=1
    for nextNode in graph[x]:
        if not visited[nextNode]:
            visited[nextNode] = True
            dfs(x)

for i in range(3):
    tmp = []
    for j in range(3):
        if i != j and computers[i][j] == 1:
            tmp.append(j+1)
    graph.append(tmp)
cnt = 0
print('graph', graph)
dfs(1)
print(cnt)
