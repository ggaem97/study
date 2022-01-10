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

def DFS(node):
    visited[node] = True
    print(node)
    for nextNode in graph[node]:
        if not visited[nextNode]:
            DFS(nextNode)

DFS(start)