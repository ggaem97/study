n = 8
visited = [False]*(n+1)
start = 1
graph = [[],
         [2,3,8],
         [1,7],
         [1,4,5],
         [3,5],
         [3,4],
         [7],
         [2,6,8],
         [1,7]]

def dfs(visited, graph, i):
    print(i, end=' ')
    visited[i] = True
    for node in graph[i]:
        if not visited[node]:
            dfs(visited, graph, node)

dfs(visited,graph,start)