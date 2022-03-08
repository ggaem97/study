def is_valid(kami):
    N = len(kami)
    if N == 1:
        return True
    mid = N // 2
    for i in range(mid):
        if kami[i] == kami[-i-1]:
            return False
    return is_valid(kami[:mid])


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        kami = input()
        if is_valid(kami):
            print("YES")
        else:
            print("NO")