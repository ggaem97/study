n = 5
grades = [2,3,1,2,2]
grades.sort()

result = 0
cnt = 0
for grade in grades:
    cnt += 1
    if cnt >= grade:
        cnt = 0
        result += 1


print(result)