from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
data = [input().strip() for _ in range(n)]
answer = ''
distance = 0
# 열을 기준으로
for j in range(m):
    gene = defaultdict(int)
    # 각각의 i번째 행에 접근
    for i in range(n):
        target = data[i][j]
        gene[target] += 1
    maxVal = max(gene.values())
    # 알파벳 순으로 정렬된 리스트 반환 sorted(~)
    for k, v in sorted(gene.items(), key=lambda x:x[0]):
        if maxVal == v:
            answer += k
            distance += (n-maxVal)
            break
print(answer)
print(distance)