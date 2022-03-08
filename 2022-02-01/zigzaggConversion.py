from math import ceil
# print(ceil(14/4))
# print(ceil(16/4))
from math import ceil
class Solution:
    def convert(s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        n = len(s)
        gap = numRows*2 -2
        p1 = 0
        p2 = gap
        if gap == 0:
            return s
        for _ in range(ceil(n/gap)):
            for i in range(0, numRows):
                if p1+i < n:
                    arr[i].append(s[p1+i])
            p1 += gap
            for i in range(numRows-2, 0, -1):
                if p2 <= n:
                    arr[i].append(s[p2-i])
            p2 += gap
        result = ''
        for i in range(numRows):
            result += "".join(arr[i])
        return result

s = Solution
print(s.convert(s="ABCDE", numRows=4))