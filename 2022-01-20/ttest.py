print('aabb'.replace('ab','',1))
a = 'aabb'
b = 'ab'
res = 0
while True:
    if a.find(b) == -1: break
    a = a.replace(b,'',1)
    print(a)
    res += 1

print(res)