1class Solution:
2    def findDifferentBinaryString(self, nums: list[str]) -> str:
3        result = []
4
5        for i in range(len(nums)):
6            if nums[i][i] == '0':
7                result.append('1')
8            else:
9                result.append('0')
10
11        return "".join(result)