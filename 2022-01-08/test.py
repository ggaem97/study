def turn_90_key(key):
    m = len(key)
    for x in range(m):
        for y in range(m):
            key[x][y] = key[m - 1 - y][x]


def check(exp_lock):
    n = len(exp_lock)//3

    for i in range(n * n):
        for j in range(n * n):
            if n <= i < 2 * n and n <= j < 2 * n:
                if exp_lock[i][j] != 1:
                    return False
    return True


def expend_lock(lock):
    n = len(lock)
    expanded_lock = [[0] * n * n for _ in range(n * n)]
    # print(expended_lock)
    for i in range(n * n):
        for j in range(n * n):
            if n <= i < 2 * n and n <= j < 2 * n:
                expanded_lock[i][j] = lock[i - n][j - n]

    return expanded_lock


def solution(key, lock):
    n = len(lock)
    m = len(key)

    for _ in range(4):
        turn_90_key(key)
        tmp = expend_lock(lock)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        tmp[x + i][y + j] += key[i][j]

                if check(tmp):
                    return True

                for i in range(m):
                    for j in range(m):
                        tmp[x + i][y + j] -= key[i][j]

        return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
         [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))