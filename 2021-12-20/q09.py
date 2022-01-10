# import heapq
# lst = []
# for i in range(3):
#     heapq.heappush(lst, i)
#
# def solution(numbers):
#     answer = ''
#     numbers = [str(number)*3 for number in numbers]
#     numbers.sort(key=lambda x:(-int(x[0]),-int(x[1]),-int(x[2])))
#     for number in numbers:
#         answer += number[:len(number)//3]
#     print(answer)
#     return answer
#

from itertools import permutations
def solution(num):
    permute = list(permutations(num,len(num)))
    print(permute)
    list_permute = [''.join(map(str,i)) for i in permute]
    answer = max(list_permute)

    return answer

print(solution([0,0,0,0]))
print(solution([100,10,565,2]))
print(solution([55,15,5,8,4,57]))


