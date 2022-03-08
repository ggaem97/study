def turnKey(key):
    m = len(key)
    # 90도 회전
    ret = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            ret[c][m - 1 - r] = key[r][c]
    return ret


def check(board, M, N):
    for i in range(N):
        for j in range(N):
            if board[M + i][M + j] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    bigLock = [[0] * (m * 2 + n) for _ in range(m * 2 + n)]
    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            bigLock[m + i][m + j] = lock[i][j]
    turned_key = key
    # 모든 방향 (4번 루프)
    for _ in range(4):
        turned_key = turnKey(turned_key)
        for i in range(1, m + n):
            for j in range(1, m + n):
                # 열쇠 넣어보기
                for r in range(m):
                    for c in range(m):
                        bigLock[i + r][j + c] += turned_key[r][c]
                # lock 가능 check
                if check(bigLock, m, n):
                    return True
                # 열쇠 빼기
                for r in range(m):
                    for c in range(m):
                        bigLock[i + r][j + c] -= turned_key[r][c]

    return False