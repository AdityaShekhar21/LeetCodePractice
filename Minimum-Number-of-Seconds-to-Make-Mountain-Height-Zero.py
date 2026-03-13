1import math
2
3class Solution:
4    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
5        
6        def can(t):
7            total = 0
8            for w in workerTimes:
9                x = int((math.sqrt(1 + 8 * t / w) - 1) // 2)
10                total += x
11                if total >= mountainHeight:
12                    return True
13            return False
14        
15        left, right = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
16        
17        while left < right:
18            mid = (left + right) // 2
19            if can(mid):
20                right = mid
21            else:
22                left = mid + 1
23        
24        return left