n = 5
count = 0
# for i in range(0, n+1):
#     if (i-3)%10 == 0:
#         count += (60*60)
#     else:
#         count = count + (15*60) + (45*15)

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)