s = '000110011111011110'
# s = '1100101'
# s = '1000101100011'
zeroCnt = 0
oneCnt = 0
for i in range(len(s)-1):
    if s[i] == '0' and s[i+1] == '1':
        zeroCnt += 1
    if s[i] == '1' and s[i+1] == '0':
        oneCnt += 1
if s[-1] == '0':
    zeroCnt += 1
else:
    oneCnt += 1

print(min(zeroCnt,oneCnt))
