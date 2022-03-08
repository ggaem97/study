lst = [3,1,6,2,7,30,1]
lst = sorted(lst)

print(lst)
a = 1
for i in range(0, sum(lst)):
    if a >= lst[i]:
        print('a', a)
        a += lst[i]
        print('after a', a)
    else:
        break
print(a)