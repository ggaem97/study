from collections import deque
import sys
sys.stdin = open('5340.txt', 'r')
for _ in range(int(input())):
    answer = []
    functions = list(input())
    n = int(input())
    data = list(input())
    arr = [data[2*i+1] for i in range(n)]
    deq = deque(arr)
    k = len(functions)
    for i, fn in enumerate(functions):
        if not deq:
            break
        if fn == 'R':
            k = len(deq)
            for i in range(k-1):
                d = deq.popleft()
                print(d)
                deq.append(d)
        else:
            deq.popleft()
    if not deq:
        print('error')
    else:
        while deq:
            answer.append(deq.popleft())
        print(answer)