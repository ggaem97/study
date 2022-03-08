import heapq
import sys
sys.stdin = open('1251.txt', 'r')

# 모든 노드를 방문하는 경로의 최소 비용 구하기
def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))

for tc in range(1, int(input())+1):
    result = 0
    n = int(input())
    xp = list(map(int, input().split()))
    yp = list(map(int, input().split()))
    island = []
    for x, y in zip(xp, yp):
        island.append((x, y))
    print(island)
    e = float(input())
    print(e)
    # 모든 노드를 연결하고 연결된 선의 가중치 구하기

    # 다익스트라 진행하기

    print(f'#{tc} {result}')