import sys
sys.stdin = open('2527.txt', 'r')

for _ in range(4):
    # 겹치는 경우로 초기화
    answer = 'a'
    points = list(map(int, input().split()))
    x1, y1, p1, q1 = points[:4]
    x2, y2, p2, q2 = points[4:]
    # 점에서 만나는 경우 + 선에서 만나는 경우
    if x2 == p1 or x1 == p2:
        if q1 == y2 or y1 == q2:
            answer = 'c'
        else:
            answer = 'b'
    if y1 == q2 or y2 == q1:
        if x1 == p2 or x2 == p1:
            answer = 'c'
        else:
            answer = 'b'
    # 안만나는 경우
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        answer = 'd'
    print(answer)