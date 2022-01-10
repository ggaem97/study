from itertools import combinations
import sys
sys.stdin = open('in4.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
box = [0]*(sum(numbers)+1)
# print(numbers)
for number in numbers:
    box[number] = 1
# print(box)
for i in range(2, n+1):
    for tup in combinations(numbers, i):
        box[sum(tup)] = 1
# print(box)

for i in range(1, len(box)):
    if box[i] == 0:
        print(i)
        break
