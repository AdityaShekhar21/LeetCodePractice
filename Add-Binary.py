1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        i, j = len(a) - 1, len(b) - 1
4        carry = 0
5        result = []
6
7        while i >= 0 or j >= 0 or carry:
8            total = carry
9
10            if i >= 0:
11                total += int(a[i])
12                i -= 1
13            if j >= 0:
14                total += int(b[j])
15                j -= 1
16
17            result.append(str(total % 2))  # current bit
18            carry = total // 2            # carry
19
20        return ''.join(reversed(result))
21