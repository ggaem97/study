for tc in range(1, int(input())+1):
    result = 1
    # 달란 트 수, 묶음 수
    n, p = map(int, input().split())
    dallant = []
    a = n // p
    b = n % p
    for _ in range(p):
        dallant.append(a)
    for i in range(b):
        dallant[i] += 1
    for d in dallant:
        result *= d
    print(f'#{tc} {result}')