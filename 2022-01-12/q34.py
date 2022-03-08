def setSoldiers():
    n = 7
    soldiers = [15,11,4,8,5,2,4]

    dp = [0]*n
    dp[n-1] = 1
    # 무조건 마지막원소 선택하게 되어있어서 비합리적
    value = soldiers[n-1]
    for i in range(n-2,-1,-1):
        if soldiers[i] >= value:
            dp[i] = dp[i+1]+1
            value = soldiers[i]
        else:
            dp[i] = dp[i+1]

    print(n - dp[0])


def setSoldiers2():
    n = 7
    soldiers = [15, 11, 4, 8, 5, 2, 4]

    dp = [0] * n
    dp[n-1] = 1
    dp[n-2] = 1
    for i in range(n-3,-1,-1):
        if soldiers[i] >= soldiers[i+1]:
            dp[i] = max(dp[i+1] + 1, dp[i])
        if soldiers[i] >= soldiers[i+2]:
            dp[i] = max(dp[i+2] + 1, dp[i])
        else:
            dp[i] = max(dp[i+1], dp[i+2])
    #     [5, 4, 3, 3, 2, 1, 1]
    # print(dp)
    print(n - dp[0])


def setSoldiers3():
    n = 7
    soldiers = [15, 11, 4, 8, 5, 2, 4]

    dp = [0]*n
    dp[n-1] = 1

    for i in range(n-2,-1,-1):
        value = soldiers[i]
        count = 1
        for j in range(n-1, i, -1):
            if value >= soldiers[j]:
                count += 1
                value = soldiers[j]
        dp[i] = count

    print(dp)


setSoldiers3()


