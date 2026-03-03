1class Solution:
2    def findKthBit(self, n: int, k: int) -> str:
3        if n == 1:
4            return "0"
5
6        length = (1 << n) - 1
7        mid = length // 2 + 1
8
9        if k == mid:
10            return "1"
11        elif k < mid:
12            return self.findKthBit(n - 1, k)
13        else:
14            mirror = length - k + 1
15            bit = self.findKthBit(n - 1, mirror)
16            return "1" if bit == "0" else "0"