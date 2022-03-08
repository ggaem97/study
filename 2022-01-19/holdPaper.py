import sys
# input = sys.stdin.readline

n = int(input())
papers = [input() for _ in range(n)]
# n = 3
# papers = ['0', '000', '1000110']

for paper in papers:
    res = True
    mid = len(paper)//2
    start = mid-1
    end = mid+1
    while start >= 0 and end <= len(paper)-1:
        if paper[start]+paper[end] in ['01', '10']:
            start -= 1
            end += 1
        else:
            res = False
            break
    if not res:
        print('NO')
    else:
        print('YES')



