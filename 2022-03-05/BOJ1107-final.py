import sys
sys.stdin = open('1107.txt', 'r')


def broken(number):
    for N in str(number):
        if N in unable:
            return False
    return True


channel = int(input())
answer = abs(100-channel)
n = int(input())
if n:
    unable = set(input().split())
for num in range(1000001):
    if not broken(num):
        answer = min(answer, len(str(num)) + abs(num-channel))
print(answer)