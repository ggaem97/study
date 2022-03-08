lst = [1,2,3,4,2,5,3,1,1,2]
n = len(lst)
cnt = 0
for i in range(n-1):
    start = i
    print('start', start)
    last = n-1
    while start <= last:
        if start == last and lst[start] == 5:
            cnt += 1
            print('last', last)
        elif lst[start] + lst[last] == 5:
            cnt += 1
            print('last', last)
        last -= 1
    print()
print(cnt)
