1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        mod = 10**9 + 7
4
5        @cache
6        def dp(zero, one, lastBit):
7            if zero == 0:
8                if lastBit == 0 or one > limit:
9                    return 0
10                else:
11                    return 1
12            elif one == 0:
13                if lastBit == 1 or zero > limit:
14                    return 0
15                else:
16                    return 1
17            if lastBit == 0:
18                res = dp(zero - 1, one, 0) + dp(zero - 1, one, 1)
19                if zero > limit:
20                    res -= dp(zero - limit - 1, one, 1)
21            else:
22                res = dp(zero, one - 1, 0) + dp(zero, one - 1, 1)
23                if one > limit:
24                    res -= dp(zero, one - limit - 1, 0)
25            return res % mod
26
27        res = (dp(zero, one, 0) + dp(zero, one, 1)) % mod
28        dp.cache_clear()
29        return res