students = {}
d = [(-1,0),(0,1),(0,-1),(1,0)]
n = int(input())
maze = [[0]*(n+1) for _ in range(n+1)]
for _ in range(n**2):
    a = list(map(int, input().split()))
    students[a[0]] = a[1:]
    tmp = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            blank = 0
            favorite = 0
            # 비어있는 칸이라면
            if maze[i][j] == 0:
                for dx, dy in d:
                    if 0<dx+i<n+1 and 0<dy+j<n+1:
                        # 인접한 칸이 비어있는 경우
                        if maze[dx+i][dy+j] == 0:
                            blank += 1
                        # 인접한 칸에 좋아하는 학생이 있는 경우
                        if maze[dx+i][dy+j] in students[a[0]]:
                            favorite += 1
                tmp.append([favorite, blank, i, j])
    # 좋아하는 학생과 가장 많이 인접한 칸, 비어있는 칸, 행, 열 기준으로 정렬
    tmp.sort(key=lambda x:(-x[0], -x[1], x[2],x[3]))
    maze[tmp[0][2]][tmp[0][3]] = a[0]

satisfied = [0, 1, 10, 100, 1000]
res = 0
for i in range(1,n+1):
    for j in range(1, n+1):
        # 인접한 칸에 앉아있는 좋아하는 학생 수
        cnt = 0
        for dx, dy in d:
            if 0<dx+i<n+1 and 0<dy+j<n+1:
                # 인접한 칸에 좋아하는 학생이 있다면
                if maze[i+dx][j+dy] in students[maze[i][j]]:
                    cnt += 1
        res += satisfied[cnt]
print(res)
