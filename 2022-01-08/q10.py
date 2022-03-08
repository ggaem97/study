key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
n = len(key)
m = len(key[0])
# 키 90도 회전
def turn_90_key():
    for x in range(n):
        for y in range(m):
            key[x][y] = key[n-1-y][x]

# 자물쇠 9x9로 확장
def expend_lock():
    expanded_lock = [[0] * m * m for _ in range(n * n)]
    # print(expended_lock)
    for i in range(n*n):
        for j in range(m*m):
            if n<=i<2*n and m<=j<2*m:
                expanded_lock[i][j] = lock[i - n][j - m]

    return expanded_lock
# for i in range(n*n):
#     print(expended_lock[i])

def check(exp_lock):
    for i in range(n*n):
        for j in range(m*m):
            if n<=i<2*n and m<=j<2*m:
                if exp_lock[i][j] != 1:
                    return False

    return True

for _ in range(4):
    turn_90_key()


    tmp = expend_lock()
    for i in range(n * n):
        for j in range(m * m):
            if n <= i < 2 * n and m <= j < 2 * m:
                tmp[i][j] += key[i - n][j - m]

    if check(tmp):
        print(True)
        break

print(False)