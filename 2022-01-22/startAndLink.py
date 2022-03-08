# 14889 스타트와 링크
from itertools import combinations
import sys
sys.stdin = open('start.txt', 'r')
n = int(input())
skills = [list(map(int, input().split())) for _ in range(n)]
team = []
cha_list = []


def teamSkill(team):
    totalSkill = 0
    for a, b in combinations(team, 2):
        totalSkill += (skills[a][b] + skills[b][a])
    return totalSkill


for i in list(combinations(range(n), n//2)):
    team.append(i)

res = 1e9
for i in range(len(team)//2):
    res = min(res, abs(teamSkill(team[i]) - teamSkill(team[-i-1])))

print(res)

