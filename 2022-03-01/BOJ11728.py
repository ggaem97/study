import sys
sys.stdin = open('11728.txt', 'r')
a, b = map(int, input().split())
data = []
for _ in range(2):
    tmp = list(map(int, input().split()))
    # 오히려 이게더 오래걸림
    while tmp:
        data.append(tmp.pop(0))
print(*sorted(data))

lst = [1,5]
lst += [5,2]
# lst.append(5)
# lst.append(2)
# input = sys.stdin.readline()
