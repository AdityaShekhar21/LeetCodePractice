1class Solution:
2    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
3        MOD = 10**9 + 7
4        
5        # dp[i][j][0] → ending with 0
6        # dp[i][j][1] → ending with 1
7        dp = [[[0,0] for _ in range(one+1)] for _ in range(zero+1)]
8        
9        for i in range(1, min(limit, zero) + 1):
10            dp[i][0][0] = 1
11        
12        for j in range(1, min(limit, one) + 1):
13            dp[0][j][1] = 1
14        
15        for i in range(zero+1):
16            for j in range(one+1):
17                
18                # end with 0
19                for k in range(1, min(limit, i) + 1):
20                    dp[i][j][0] = (dp[i][j][0] + dp[i-k][j][1]) % MOD
21                
22                # end with 1
23                for k in range(1, min(limit, j) + 1):
24                    dp[i][j][1] = (dp[i][j][1] + dp[i][j-k][0]) % MOD
25        
26        return (dp[zero][one][0] + dp[zero][one][1]) % MOD