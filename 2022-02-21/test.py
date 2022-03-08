import sys
sys.stdin = open('5340.txt', 'r')

for _ in range(int(input())):
    fn = input()
    # 두 번 뒤집는 경우 제외
    fn.replace("RR", '')
    n = int(input())
    # data = input()
    arr = list(map(str, input()[1:-1].split(',')))
    # arr = [data[i * 2 + 1] for i in range(n)]
    D_front, D_back, check = 0, 0, True
    for key in fn:
        if key == 'R':
            check = not check
        elif key == 'D':
            if check:
                D_front += 1
            else:
                D_back += 1

    if D_front + D_back <= n:
        arr = arr[D_front:n - D_back]
        if not check:
            arr.reverse()
        print('[' + ','.join(arr) + ']')
    else:
        print("error")


