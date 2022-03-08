import sys
sys.stdin = open('a3.txt', 'r')

unit = ['백','십','억','천만','백','십','만','천','백','십','']
dic = {1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구'}
n = int(input())
for _ in range(n):
    word = ''
    number = list(map(int, input()))
    print(number)
    k = len(number)
    for i in range(k):
        if number[i] == 1 and i != k-1:
            word = word + (unit[-k+i])
        else:
            word = word + (dic[number[i]] + unit[-k+i])
    print(word)

