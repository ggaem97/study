import sys
sys.stdin = open('5201.txt', 'r')

for tc in range(1, int(input())+1):
    answer = 0

    # 컨테이너 수, 트럭 수
    w, t = map(int, input().split())
    # 화물의 무게
    weight = list(map(int, input().split()))
    # 트럭의 적재 가능용량
    truck = list(map(int, input().split()))
    weight.sort(key=lambda x:-x)
    truck.sort(key=lambda x:-x)
    print(weight)
    print(truck)
    pointer = 0
    for i in range(t):
        for pointer in range(w):
            if truck[i] < weight[pointer]:
                continue
            answer += weight[pointer]
            weight = weight[pointer+1:] if pointer+1<w else []
            break
        # for j in range(w):
        #     if not weight:
        #         break
        #     if weight[j] > truck[i]:
        #         continue
        #     print('무게를 담을 수 있어요')
        #     result += weight[j]
        #     print(result)
        #     weight = weight[1:]

    print(f'#{tc} {answer}')