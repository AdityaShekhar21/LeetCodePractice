1class Solution:
2    def isTrionic(self, nums: list[int]) -> bool:
3        n = len(nums)
4        if n < 4:
5            return False
6
7        i = 0
8
9        # strictly increasing
10        while i + 1 < n and nums[i] < nums[i + 1]:
11            i += 1
12        if i == 0 or i == n - 1:
13            return False
14
15        # strictly decreasing
16        while i + 1 < n and nums[i] > nums[i + 1]:
17            i += 1
18        if i == n - 1:
19            return False
20
21        # strictly increasing again
22        while i + 1 < n and nums[i] < nums[i + 1]:
23            i += 1
24
25        return i == n - 1
26