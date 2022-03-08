import sys
sys.stdin = open('watch.txt', 'r')

n = int(input())
hall = [list(input().split()) for _ in range(n)]

teachers = []
for i in range(n):
    for j in range(n):
        if hall[i][j] == "T":
            teachers.append((i, j))

move = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def wall_check():
    for teacher in teachers:
        for i in range(4):
            x, y = teacher
            while 0 <= x < n and 0 <= y < n:
                if hall[x][y] == "O":
                    break
                elif hall[x][y] == "S":
                    return False

                x += move[i][0]
                y += move[i][1]

    return True


chk = False


def dfs(depth):
    global chk

    if not chk:
        if depth == 3:
            if wall_check():
                chk = True

            return

        for i in range(n):
            for j in range(n):
                if hall[i][j] == "X":
                    hall[i][j] = "O"
                    dfs(depth + 1)
                    hall[i][j] = "X"


dfs(0)
print("YES" if chk else "NO")