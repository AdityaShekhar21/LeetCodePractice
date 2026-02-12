1class Solution:
2    def minimumCost(self, nums: list[int]) -> int:
3        rest = sorted(nums[1:])
4        return nums[0] + rest[0] + rest[1]
5