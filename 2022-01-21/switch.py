# import sys
# sys.stdin = open('switch.txt','r')
# n = int(input())
# state = list(input())
# target = list(input())
#
#
# def change_zero(light):
#     cnt = 1
#     light[0] = str(1 - int(light[0]))
#     light[1] = str(1 - int(light[1]))
#
#     for i in range(1, len(light)):
#         if light[i-1] == target[i-1]:
#             continue
#         else:
#             cnt += 1
#             light[i-1] = str(1-int(light[i-1]))
#             light[i] = str(1 - int(light[i]))
#             if i < len(light)-1:
#                 light[i+1] = str(1- int(light[i+1]))
#     if target == light:
#         return cnt
#
#     return 200002
#
#
# def non_change_zero(light):
#     cnt = 0
#     for i in range(1, len(light)):
#         if light[i-1] == target[i-1]:
#             continue
#         else:
#             cnt += 1
#             light[i-1] = str(1 - int(light[i-1]))
#             light[i] = str(1 - int(light[i]))
#             if i < len(light)-1:
#                 light[i+1] = str(1 - int(light[i+1]))
#
#     if target == light:
#         return cnt
#
#     return 100002
#
#
# cnt1 = change_zero(state[:])
# cnt2 = non_change_zero(state[:])
#
# ans = min(cnt1, cnt2)
# if ans == 100002:
#     ans = -1
# print(ans)
