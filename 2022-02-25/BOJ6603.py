from itertools import combinations
import sys
sys.stdin = open('6603.txt', 'r')

while True:
    s = list(map(int, input().split()))
    if len(s) == 1 and s == [0]:
        break
    k = s.pop(0)
    for data in list(combinations(s, 6)):
        print(*data)
    print()