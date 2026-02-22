1class Solution:
2    def binaryGap(self, n: int) -> int:
3        prev = -1
4        max_gap = 0
5        position = 0
6
7        while n > 0:
8            if n & 1:
9                if prev != -1:
10                    max_gap = max(max_gap, position - prev)
11                prev = position
12            n >>= 1
13            position += 1
14
15        return max_gap