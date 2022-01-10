n, m, k = 5,8,3
numbers = [2,4,5,4,6]
numbers.sort()
answer = 0
first = numbers[-1]
second = numbers[-2]

# for i in range(1, m+1):
#     if i%(k+1) == 0:
#         answer += second
#     else:
#         answer += first

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         m -= 1
#         answer += first
#     if m == 0:
#         break
#     m -= 1
#     answer += second

count = m//(k+1)*k + m%(k+1)
# print(count)
# print(first)
answer += count*first
# print(answer)
count = m//(k+1)
answer += count*second

print(answer)