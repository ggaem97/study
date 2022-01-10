import sys
sys.stdin = open('in4.txt','r')

s = input()
cols = ['','a','b','c','d','e','f','g''h']
n = int(s[1])
# print(chr(97))
# m = cols.index(s[0])
m = int(ord(s[0])) - int(ord('a')) + 1
print(n,m)
cnt = 0
moves = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(2,-1),(-2,1),(2,1)]
for i in range(8):
    x, y = moves[i]

    if 1<=(n+x)<=8 and 1<=(m+y)<=8:
       cnt += 1
print(cnt)
