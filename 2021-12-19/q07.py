import sys
sys.stdin = open('in4.txt','r')
a = int(input())
s = str(a)
l = len(s)
left = s[:l]
right = s[l:]
leftLst = [int(l) for l in left]
rightLst = [int(r) for r in right]
if sum(leftLst) == sum(rightLst):
    print("LUCKY")
else:
    print("READY")

