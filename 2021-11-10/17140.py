import sys
sys.stdin = open('in.txt','r')
r,c,k = map(int, input().split())
a = [[0]+list(map(int, input().split())) for _ in range(3)]
a.insert(0,[0,0,0,0])
for lst in a:
    print(lst)
check = True
def rowFn(rows):
    for row in rows:
        pass
    pass
def colFn(cols):
    pass

def arrange():
    pass

for i in range(100):
    n=len(a)
    m=len(a[0])
    if a[r+1][c+1]==2:
        check=False
        print(i)
        break

    if n>=m:
        rowFn(a)
    else:
        colFn(a)

if check:
    print(-1)