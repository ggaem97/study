n = int(input())
data = list(map(int,input().split()))
data.sort()
answer = 0
pre = 0
# for i in range(n):
#     result += sum(data[:i+1])
# print(result)
# print(sum(sum(data[:i+1]) for i in range(n)))
print(sum([data[i]*(n-i) for i in range(n)]))
print(sum([data[i]*(n-i) for i in reversed(range(n))]))