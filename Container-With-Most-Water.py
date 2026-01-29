1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        left, right = 0, len(height) - 1
4        max_area = 0
5
6        while left < right:
7            width = right - left
8            curr_height = min(height[left], height[right])
9            max_area = max(max_area, width * curr_height)
10
11            if height[left] < height[right]:
12                left += 1
13            else:
14                right -= 1
15
16        return max_area
17