import sys
sys.stdin = open('1969.txt', 'r')
n,m = map(int, input().split())
dna = []
refer1 = {'A':0,'C':1,'G':2,'T':3}
refer2 = ['A','C','G','T']
cnt = [[0]*4 for _ in range(m)]
comb = []

for i in range(n):
    a = input()
    dna.append(a)
    for j in range(m):
        cnt[j][refer1[a[j]]] += 1

print(cnt)
print(dna)

smallest = ''
answer = 0
for rowLst in cnt:
    print('rowLst', rowLst)
    c = max(rowLst)
    for j in range(4):
        if rowLst[j] == c:
            smallest += refer2[j]
            break
    answer += (n - c)
print(smallest)
print(answer)