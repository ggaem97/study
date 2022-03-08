s = "aabbaccc"

n = len(s)
answer = n
for step in range(1, n//2+1):
    pre = s[0:step]
    count = 1
    compress = ""
    for i in range(step, n, step):
        now = s[i:i+step]
        if pre == now:
            count += 1
        else:
            compress += str(count) + pre if count >=2 else pre
            count = 1
            pre = now
            # print('compress', compress)
    compress += str(count) + pre if count >= 2 else pre
    answer = min(answer, len(compress))
    print(compress)
print(answer)