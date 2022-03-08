import sys
sys.stdin = open('watch.txt', 'r')

n = int(input())
hall = [[] for _ in range(n)]
teachers = []
for i in range(n):
    hall[i] = input().split()
    for j, person in enumerate(hall[i]):
        if person == 'T': teachers.append((i,j))


def watch():
    d = [(1,0),(0,1),(0,-1),(-1,0)]
    global hall
    for teacher in teachers:
        for dx, dy in d:
            x, y = teacher
            while 0<=x<n and 0<=y<n:
                if hall[x][y] == 'O':
                    break
                elif hall[x][y] == 'S':
                    return True
                x += dx
                y += dy
    return False


res = False
def DFS(count):
    global res
    if count == 3:
        # 학생이 한명도 안걸리면
        if not watch():
            res = True
            return
    else:
        for x in range(n):
            for y in range(n):
                if hall[x][y] == 'X':
                    hall[x][y] = 'O'
                    DFS(count+1)
                    hall[x][y] = 'X'

DFS(0)
if res:
    print("YES")
else:
    print("NO")