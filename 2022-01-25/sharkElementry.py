import sys
sys.stdin = open('shark.txt', 'r')

d = [(0,1),(1,0),(0,-1),(-1,0)]
n = int(input())
maze =[[0]*(n+1) for _ in range(n+1)]
student = {}
for _ in range(n*n):
    a = list(map(int,input().split()))
    student[a[0]] = a[1:]
    tmp =[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            blank = 0
            friend = 0
            if maze[i][j] == 0:
                for dx,dy in d:
                    if 0<i+dx<n+1 and 0<j+dy<n+1:
                        if maze[i+dx][j+dy] == 0:
                            blank+=1
                        if maze[i+dx][j+dy] in a:
                            friend+=1
                tmp.append([friend,blank,i,j])
    tmp.sort(key= lambda x : (-x[0],-x[1],x[2],[3]))
    print('sorted tmp', tmp)
    maze[tmp[0][2]][tmp[0][3]] = a[0]
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(maze[i][j], end=' ')
        print()
m = [0,1,10,100,1000]
sum = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        count = 0
        for dx,dy in d:
            if 0<i+dx<n+1 and 0<j+dy<n+1:
                if maze[i+dx][j+dy] in student[maze[i][j]]:
                    count+=1
        sum+=m[count]
print(sum)
