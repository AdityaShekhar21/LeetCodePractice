1class Solution:
2    def hasAllCodes(self, s: str, k: int) -> bool:
3        seen = set()
4
5        for i in range(len(s) - k + 1):
6            seen.add(s[i:i+k])
7            if len(seen) == (1 << k):  # 2^k
8                return True
9
10        return len(seen) == (1 << k)