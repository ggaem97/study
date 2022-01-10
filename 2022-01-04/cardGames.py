import sys

sys.stdin = open('in.txt','r')
n,m = map(int, input().split())

result = 0
for _ in range(n):
    board = list(map(int, input().split()))
    min_value = min(board)
    result = max(result, min_value)
print(result)

