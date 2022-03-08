import sys
sys.stdin = open('container.txt', 'r')

# 작은 높이를 선택해야하는 이유?
def solution(height):
    start = 0
    end = len(height)-1
    dist = (end-start)*(min(height[start], height[end]))
    while start < end:
        if height[start] < height[end]:
            start += 1
        else:
            end -= 1
        dist = max(dist, (end-start)*min(height[start], height[end]))

    return dist


lst = list(map(int, input().split(',')))
print(solution(height=lst))



