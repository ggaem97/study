import sys
sys.stdin = open('in.txt','r')

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    data = int(sys.stdin.readline())
    print('data> ',data)
    h.sort(key=lambda x:(x[0],-x[1]))
    print('sorted h>',h)
    if data !=0:
        if not h:
            h.append((abs(data),1))
            print('hh append', h)
            continue
        for he in h:
            if data<0 and he[0] == -data:
                idx = h.index(he)
                h.pop(idx)
                h.append((abs(data),2))
                print('h append', h)
                break
        else:
            h.append((abs(data),1))
            print('hhh append', h)

    else:
        if h:
            if h[-1][1] == 2:
                tmp = h.pop(0)[0]
                print(-tmp)
                h.append((abs(tmp),1))
                print('h>',h)
            else:
                print(h.pop(0)[0])
        else:
            print(0)

