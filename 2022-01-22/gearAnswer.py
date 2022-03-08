import sys
sys.stdin = open('gear.txt', 'r')

mat = []
for i in range(0,4):
    x=str(input())
    mat.append(x)
print(mat)
k = int(input())
for _ in range(k):
    num, direction=map(int, input().split())
    num-=1
    check = [0]*4
    check[num]=direction
    for i in range(num, 3):
        if mat[i][2]!=mat[i+1][6]:
            check[i+1]=check[i]*(-1)
        else:
            break
    for i in range(num, 0, -1):
        if mat[i][6]!=mat[i-1][2]:
            check[i-1]=check[i]*(-1)
        else:
            break
    print(check)
    for i in range(4):
        if check[i]==1:
            mat[i]=mat[i][7]+mat[i][:7]
        elif check[i]==-1:
            mat[i]=mat[i][1:]+mat[i][0]
print(mat)
ans=0
for i in range(4):
    ans += int(mat[i][0])*pow(2,i)
print(ans)