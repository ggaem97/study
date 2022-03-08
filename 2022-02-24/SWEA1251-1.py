import heapq
import sys
sys.stdin = open('1251.txt', 'r')
# https://mungto.tistory.com/225

# 모든 노드를 방문하는 경로의 최소 비용 구하기
def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))


# 각 선분의 가중치를 구하는 함수
def makeDistance():
    for i in range(n):
        for j in range(i+1, n):
            d = ((xp[i] - xp[j])**2 + (yp[i] - yp[j])**2)
            heapq.heappush(distance, (d, i, j))


for tc in range(1, int(input())+1):
    result = 0
    n = int(input())
    xp = list(map(int, input().split()))
    yp = list(map(int, input().split()))
    e = float(input())
    print(e)
    # 모든 노드를 연결하고 연결된 선의 가중치 구하기
    distance = []
    makeDistance()
    # 다익스트라 진행하기

    print(f'#{tc} {result}')