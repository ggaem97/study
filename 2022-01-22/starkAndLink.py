from itertools import combinations
import sys
sys.stdin = open('start.txt', 'r')
n = int(input())
skills = [list(map(int, input().split())) for _ in range(n)]
print(skills)


# 어떻게 두 팀으로 나눌까
def divideTeam():
    res = []
    nums = [i for i in range(n)]
    for data in list(combinations(nums, n//2)):
        t_nums = nums[:]
        for num in data:
            t_nums.remove(num)
        if (tuple(t_nums), data) in res:
            continue
        res.append((tuple(t_nums), data))

    print(res)



# 각 팀끼리의 능력치 차이의 최솟값을 어떻게 구할까




