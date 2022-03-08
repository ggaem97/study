def turnKey(key):
    m = len(key)
    # 90도 회전
    ret = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            ret[c][m - 1 - r] = key[r][c]
    return ret


def checkBigLock(bigLock, m, n):
    for i in range(n):
        for j in range(n):
            if bigLock[i+m-1][j+m-1] != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)
    bigLock = [[0] * (n + 2 * m - 2) for _ in range((n + 2 * m - 2))]

    # 큰 자물쇠 세팅
    for i in range(n):
        for j in range(n):
            bigLock[i + m - 1][j + m - 1] = lock[i][j]
    # 키 90, 180, 270 회전시켜 보기
    for _ in range(4):
        turn_key = turnKey(key)
        # 큰 자물쇠에 turn_key 뿌리기
        for i in range(0, n+m-1):
            for j in range(0, n+m-1):
                for r in range(m):
                    for c in range(m):
                        bigLock[i + r][j + c] += turn_key[r][c]
                # 자물쇠가 맞지 않으면
                if not checkBigLock(bigLock, m, n):
                    # 큰 자물쇠 원상태로 되돌리기
                    for r in range(m):
                        for c in range(m):
                            bigLock[i + r][j + c] -= turn_key[r][c]
                # 자물쇠가 맞으면 true 리턴
                else:
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))

