from itertools import combinations
n = 10
box = [2,3,5]

# 문제점 : combination 조합에서 자기 자신이 두 번인 경우는 포함되지 않음
def findUgly():
    for a,b in list(combinations(box,2)):
        box.append(a*b)

    for i in range(3,6):
        for j in range(3):
            box.append(box[i]*box[j])

    for i in range(6,8):
        for j in range(3):
            box.append(box[i]*box[j])

    for i in range(9,11):
        for j in range(3):
            box.append(box[i]*box[j])

    for i in range(11,13):
        for j in range(3):
            box.append(box[i]*box[j])

    return box

# 못생긴 수 : 정렬 과정 거쳐야 함
def uglyNumber():
    n = 10
    primes = [2,3,5]
    box = [1]

    i = 0
    while len(box) <= n:
        for prime in primes:
            data = box[i]*prime
            if not data in box:
                box.append(data)
        i += 1

    box.sort()
    return box[n-1]


def realUglyNumber():
    primes = [2,3,5]



realUglyNumber()





