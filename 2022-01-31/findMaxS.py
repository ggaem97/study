class Solution:
    def maxArea(self, height: list[int]) -> int:
        dist = len(height) - 1
        # 길이가 2인 경우
        if len(height) == 2:
            return min(height)
        # 양쪽 끝 값이 같은 경우
        elif height[0] == height[-1]:
            return dist * height[0]
        start = 0
        end = len(height) - 1
        # 투포인터 문제점 : 변수에 최대 깊이를 저장하는 방식을 떠올리지 못함
        # 반례 : [1,2,4,3]
        # 투 포인터란? 일차원 배열에서 서로 다른 원소를 가리키는 두 개의 포인터를 조작하면서 구하고자 하는 값을 얻는 것
        # 구하고자 하는 것 ? 최대 깊이 > 최대 깊이 어떻게 저장 ? > 투포인터와 max 함수 이용
                                                        # > 이중 for문 이용 (효율성 구림)
        while start < end:
            if height[start] < height[end] and start + 1 != end:
                if height[start] < height[start + 1]:
                    start += 1
                    dist -= 1
                    continue
                else:break
            elif height[end] < height[start] and end - 1 != start:
                if height[end] < height[end - 1]:
                    end -= 1
                    dist -= 1
                    continue
                else:break
            else:break

        h = min(height[start], height[end])
        return dist * h


    def maxArea1(self, height: list[int]) -> int:
        start = 0
        end = len(height)-1
        dist = end - start
        max_area = dist * min(height[start], height[end])
        while start < end:
            if height[start] <= height[end]:
                start += 1
                dist -= 1
            else:
                end -= 1
                dist -= 1
            max_area = max(max_area, dist*min(height[start], height[end]))

        return max_area
s=Solution()
# print(s.maxArea(height=[1,8,6,2,5,4,8,3,7]))
print(s.maxArea(height=[1,2,4,3]))
