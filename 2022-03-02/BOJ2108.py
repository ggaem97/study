from collections import Counter
import sys
sys.stdin = open('2108.txt', 'r')

n = int(input())
nums = [int(input()) for _ in range(n)]
print(round(sum(nums)/n)) # 산술평균
nums.sort()
print(nums[n//2]) # 중앙값
# 최빈값 구하기
countDic = Counter(nums)
# 최빈값을 가지는 키 구하기
maxCntKey = [k for k, v in countDic.items() if max(countDic.values()) == v]
# 최빈값 구하기
if len(maxCntKey) >= 2:
    # 두번째로 작은 값 출력
    print(sorted(maxCntKey)[1])
else:
    print(maxCntKey[0])
print(max(nums)-min(nums)) # 범위
