1class Solution:
2    def minOperations(self, s: str) -> int:
3        changes_start_0 = 0
4        changes_start_1 = 0
5
6        for i, ch in enumerate(s):
7            expected0 = '0' if i % 2 == 0 else '1'
8            expected1 = '1' if i % 2 == 0 else '0'
9
10            if ch != expected0:
11                changes_start_0 += 1
12            if ch != expected1:
13                changes_start_1 += 1
14
15        return min(changes_start_0, changes_start_1)