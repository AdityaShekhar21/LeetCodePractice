1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        x = n ^ (n >> 1)
4        return (x & (x + 1)) == 0
5