import sys

sys.stdin = open('in1.txt','r')

s = list(input())
alpha = []
integer = 0
# print(ord('A'))
# print(ord('Z'))
for data in s:
    summary = 0
    if 65<= ord(data) <= 90:
        alpha.append(data)
    else:
        integer += int(data)
alpha.sort()
result = ''.join(alpha) + str(integer)
print(result)


