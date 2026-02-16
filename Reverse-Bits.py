1class Solution:
2    def reverseBits(self, n: int) -> int:
3        result = 0
4
5        for _ in range(32):
6            result <<= 1          # make space for next bit
7            result |= (n & 1)     # add last bit of n
8            n >>= 1               # remove last bit from n
9
10        return result
11