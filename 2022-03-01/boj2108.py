import sys
sys.stdin = open('2108.txt', 'r')
n = int(input())
data = [int(input()) for _ in range(n)]
data.sort()
print(round(sum(data)/n))
print(data[n//2])
# 최빈값 컨트롤에서 막힘 
dic = {}
for d in data:
    if d in dic.keys():
        dic[d] += 1
    else:
        dic[d] = 1
print(dic)
maxVal = max(dic.values(), key=lambda x:x)
print(maxVal)
dicVal = list(dic.values())
dicValSet = set(dicVal)
print(dicValSet)
# if dicVal.count(maxVal) >= 2:
#     print(dicValSet[1])
# else:
#     print(dicValSet[0])

# if dicVal.count(maxVal) >=
# print(max(data, key=lambda x:data.count(x))) # 이렇게 하면 중복일 경우 에러 발생
print(max(data)-min(data))