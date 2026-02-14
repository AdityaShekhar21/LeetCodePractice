1class Solution:
2    def minimumDifference(self, nums: list[int], k: int) -> int:
3        if k == 1:
4            return 0
5
6        nums.sort()
7        min_diff = float('inf')
8
9        for i in range(len(nums) - k + 1):
10            diff = nums[i + k - 1] - nums[i]
11            min_diff = min(min_diff, diff)
12
13        return min_diff
14