import sys
sys.stdin = open('5201.txt')
for tc in range(1, int(input())+1):
    # print(f'#{tc} start')
    answer = 0
    # 컨테이너수, 트럭수
    n, m = map(int, input().split())
    # n개의 화물의 무게
    weight = list(map(int, input().split()))
    # m개 트럭의 적재용량
    truck = list(map(int, input().split()))
    truck.sort(key=lambda x:x, reverse=True)
    weight.sort(key=lambda x:x, reverse=True)
    # print('truck', truck)
    # print('weight', weight)
    for i in range(n):
        # print('target is', weight[i])
        # 더이상 컨테이너를 담을 트럭이 없는 경우
        if i > m-1:
            break
        for j in range(m):
            # 트럭이 비어있다면
            if not truck:
                break
            if truck[0] >= weight[i]:
                answer += weight[i]
                truck.pop(0)
                break
    # print('result:', result)
    print(f'#{tc} {answer}')