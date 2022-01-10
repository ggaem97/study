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
visited[start] = True
stack = [start]
print(stack[-1])
while stack:
    i = stack[-1]
    for node in graph[i]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)
            print(stack[-1])
            break
    else:
        stack.pop()


