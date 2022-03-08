class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 1
        ss = []
        # 0부터 n-1에 대해
        for start in range(0, n):
            # 부분 문자열에 등장한 단어인 경우
            if s[start] in ss:
                # 그 위치까지 이전 s를 자른다
                idx = ss.index(s[start])
                ss = ss[idx+1:]
                ss.append(s[start])
            # 등장하지 않은 경우
            else:
                # 부분문자열에 붙인다
                ss.append(s[start])
            maxLen = max(maxLen, len(ss))
        return maxLen

s = Solution()
print(s.lengthOfLongestSubstring("aabaab!bb"))