n = 3
m = 4
a = [[1,3,3,2],[2,1,4,1],[0,6,4,7]]


# 각 열에서 최대값만 뽑는 경우
def bigSum():
    answer = 0
    for j in range(m):
        data = 0
        # x,y 정보 사용 안했음 > 가장 큰 금광 값만 계속 가져 가려면 반드시 필요함
        # 즉, 알맞은 알고리즘이 아님
        x, y = 0, 0
        for i in range(n):
            if a[i][j] > data:
                x = i
                y = j
                data = a[i][j]
        answer += data

    return answer


def goldMining():
    data = 0
    x, y = 0, 0
    # 첫번째 가장 큰 금광 찾기
    for i in range(n):
        if data < a[i][0]:
            data = a[i][0]
            x = i
    answer =0
    answer += a[x][y]
    # 나머지 금광 찾기
    for j in range(1, m):
        data = 0
        xx, yy = 0,0
        if x+1 < n and y+1 < m and data < a[x+1][y+1]:
            data = a[x+1][y+1]
            xx = x + 1
            yy = y + 1
        if x-1 < n and y+1 < m and data < a[x-1][y+1]:
            data = a[x-1][y+1]
            xx = x-1
            yy = y+1
        if x < n and y+1 < m and data < a[x][y+1]:
            data = a[x][y+1]
            xx = x
            yy = y+1
        answer += a[xx][yy]
        x, y = xx, yy
        # print(x, y)

    return answer

# print(goldMining())

import sys
sys.stdin = open('q31','r')
def realGoldMining():
    # dp 테이블을 2차원으로 만들 것!
    k = int(input())
    n, m = 0,0
    dp = []
    for _ in range(k):
        dp = []
        n, m = map(int, input().split())
        data = list(map(int, input().split()))
        while data:
            lst = []
            for _ in range(m):
                lst.append(data.pop(0))
            dp.append(lst)
        # print('dp', dp)

        for y in range(1, m):
            for x in range(n):
                maxVal = 0
                if 0<=x-1<n and 0<=y-1<m:
                    maxVal = max(dp[x-1][y-1], maxVal)
                if 0<=x<n and 0<=y-1<m:
                    maxVal = max(dp[x][y-1], maxVal)
                if 0<=x+1<n and 0<=y-1<m:
                    maxVal = max(dp[x+1][y-1], maxVal)
                dp[x][y] = maxVal + dp[x][y]

        # print('after dp', dp)

        result = 0
        for i in range(n):
            result = max(result, dp[i][m-1])
        print(result)


realGoldMining()






