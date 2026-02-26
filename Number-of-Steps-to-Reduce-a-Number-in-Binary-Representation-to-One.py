1class Solution:
2    def numSteps(self, s: str) -> int:
3        steps = 0
4        carry = 0
5
6        # Traverse from right to left (except first digit)
7        for i in range(len(s) - 1, 0, -1):
8            bit = int(s[i]) + carry
9
10            if bit == 1:
11                steps += 2      # +1 then /2
12                carry = 1
13            else:
14                steps += 1      # just /2
15
16        return steps + carry