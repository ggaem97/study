from bisect import bisect_left, bisect_right


def count_by_value(arr, left_val, right_val):
    left_idx = bisect_left(arr, left_val)
    right_idx = bisect_right(arr, right_val)
    print('left_idx',left_idx,'right_idx',right_idx)
    return right_idx - left_idx


def solution(words, queries):
    array = [[] for _ in range(10001)]
    reversedArr = [[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reversedArr[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversedArr[i].sort()

    print(array[:8])
    print(reversedArr[:8])
    result = []
    for query in queries:
        if query[0] != '?':
            left = query.replace('?', 'a')
            right = query.replace('?', 'z')
            print('left', left)
            print('right', right)
            count = count_by_value(array[len(query)], left, right)
            result.append(count)
            print(result)
        else:
            left = query[::-1].replace('?', 'a')
            right = query[::-1].replace('?', 'z')
            print('left', left)
            print('right', right)
            count = count_by_value(reversedArr[len(query)], left, right)
            result.append(count)
            print(result)
    print(result)

solution(["frodo", "front", "frost", "frozen", "frame", "kakao"]
         , ["fro??", "????o", "fr???", "fro???", "pro?"])