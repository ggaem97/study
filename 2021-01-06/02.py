s = '0271'
output = 15
# answer = int('3') + int('5')
# print(answer)
# 실수 : 1인 경우에도 곱하기 보다는 더하기가 더 효율적임
answer = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    # answer 처리 + 1인 경우에도 처리
    if num <= 1 or answer <= 1:
        answer += int(s[i])
    else:
        answer *= int(s[i])
# answer = 0 if int(s[0]) in ('0', '1') else 1
#
# for word in s:
#     if word in ('0', '1'):
#         answer += int(word)
#     else:
#         answer *= int(word)
print(answer)

