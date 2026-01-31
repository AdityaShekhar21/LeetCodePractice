1from collections import Counter
2
3class Solution:
4    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
5        freq = Counter(nums)
6        buckets = [[] for _ in range(len(nums) + 1)]
7
8        for num, count in freq.items():
9            buckets[count].append(num)
10
11        result = []
12        for i in range(len(buckets) - 1, 0, -1):
13            for num in buckets[i]:
14                result.append(num)
15                if len(result) == k:
16                    return result
17