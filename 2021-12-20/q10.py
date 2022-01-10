def solution(n, times):
    answer = 0

    start = 1
    last = n * max(times)

    while start <= last:
        mid = (start + last) // 2

        passedPeople = sum(mid // time for time in times)
        print(passedPeople)
        if passedPeople < n:
            left = mid + 1
            print("left++")
        else:
            last = mid - 1
            print("last--")
            answer = mid

    return answer


print(solution(6,[7,10]))