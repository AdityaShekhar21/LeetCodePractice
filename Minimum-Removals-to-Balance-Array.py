1class Solution:
2    def minRemoval(self, nums: list[int], k: int) -> int:
3        nums.sort()
4        n = len(nums)
5
6        left = 0
7        max_len = 0
8
9        for right in range(n):
10            while nums[right] > nums[left] * k:
11                left += 1
12            
13            max_len = max(max_len, right - left + 1)
14
15        return n - max_len
16