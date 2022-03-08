def is_holdingPaper(paper):
    N = len(paper)
    if N == 1:
        return True
    mid = N//2
    for i in range(mid):
        if paper[i] == paper[-i - 1]:
            return False
    return is_holdingPaper(paper[:mid])


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline
    n = int(input().strip())
    for _ in range(n):
        p = input().strip()
        if is_holdingPaper(p):
            print('YES')
        else:
            print('NO')


