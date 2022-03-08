import sys
sys.stdin = open('i.txt', 'r')

n = int(input())
answer = n
for _ in range(n):
    check = []
    word = input()
    for w in word:
        if w in check:
            if check[-1] == w:
                continue
            answer -= 1
            break
        check.append(w)
print(answer)