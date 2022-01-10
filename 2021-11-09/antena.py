import sys
sys.stdin = open('in.txt','r')
n = int(input())
houses = list(map(int, input().split()))
distance = {}
for i in range(n):
    target=houses[i]
    sum=0
    for house in houses:
        if target == house:
            continue
        else:
            sum += abs(target-house)
    distance[target]=sum

m = min(distance.values())
for k,v in distance.items():
    if v == m:
        print(k)
        break