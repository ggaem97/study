n, m = map(int, input().split())
arr = [0]
num = 0
while len(arr) <= m:
    num += 1
    for _ in range(num):
        arr.append(num)

# 시간 복잡도 : O(m+1-n)
# 시간 복잡도 : O(m-n)
# ex) arr[1:5] -> O(4)
print(sum(arr[n:m+1]))