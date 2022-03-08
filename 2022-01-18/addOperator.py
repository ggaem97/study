import sys
# input = sys.stdin.readline
sys.stdin = open('in.txt', 'r')

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = list(map(int, input().split()))
operatorCnt = add + sub + mul + div
mxVal = -1e9
minVal = 1e9


def DFS(summary, count):
    global mxVal, minVal
    global add, sub, mul, div

    if add > 0:
        add -= 1
        count += 1
        DFS(summary+numbers[count], count)
        count -= 1
        add += 1
    if sub > 0:
        sub -= 1
        count += 1
        DFS(summary-numbers[count], count)
        count -= 1
        sub += 1
    if mul > 0:
        mul -= 1
        count += 1
        DFS(summary*numbers[count], count)
        count -= 1
        mul += 1
    if div > 0:
        div -= 1
        count += 1
        DFS(int(summary/numbers[count]), count)
        count -= 1
        div += 1

    if count == operatorCnt:
        mxVal = max(mxVal, summary)
        minVal = min(minVal, summary)


DFS(numbers[0], 0)
print(mxVal)
print(minVal)