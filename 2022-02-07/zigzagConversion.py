from math import ceil
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        n = len(s)
        gap = numRows*2-2
        p1 = 0
        p2 = gap
        # numRows 값이 1인 경우
        if gap == 0:
            return s
        # numRows 값이 2이상인 경우 반복문 동작
        for _ in range(ceil(n/gap)):
            # 지그재그 중 '|' 부분
            for i in range(0, numRows):
                if p1+i < n:
                    arr[i].append(s[p1+i])
            p1 += gap
            # 지그재그 중 '\' 혹은 '/' 부분
            for i in range(numRows-2, 0, -1):
                if p2-i < n:
                    arr[i].append(s[p2-i])
            p2 += gap
        result = ''
        # 각 행에 담긴 문자열을 하나로 합치기
        for i in range(numRows):
            result += "".join(arr[i])
        return result

s = Solution()
print(s.convert("PAYPALISHIRING", 3))