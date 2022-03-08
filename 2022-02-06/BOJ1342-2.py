import sys
sys.stdin = open('1342.txt')
s = input()
alpha = [0 for _ in range(26)]
for word in s:
    alpha[(ord(word)-97)] += 1


def backtracking(count, picked):
    global result
    if count == 0:
        result += 1
    for i in range(26):
        if alpha[i] > 0 and i != picked:
            alpha[i] -= 1
            backtracking(count-1, i)
            alpha[i] += 1


result = 0
backtracking(len(s), -1)
print(result)