from collections import deque
import sys
sys.stdin = open('input.txt', 'r')
for tc in range(1, int(input())+1):
    answer = 0
    n = int(input())
    time = [tuple(map(int, input().split())) for _ in range(n)]
    # 일찍 칼퇴하는 순으로 정렬, 칼퇴 시간이 같을 경우 시작 시간을 정렬
    time.sort(key=lambda x:(x[1], x[0]))
    for i in range(n):
        deq = deque(time)
        pre = deq.popleft()
        lst = [pre]
        while deq:
            if pre[1] <= deq[0][0]:
                pre = deq.popleft()
                lst.append(pre)
                continue
            deq.popleft()
        answer = max(answer, len(lst))
        if time:
            time.pop(0)

    print(f'#{tc} {answer}')