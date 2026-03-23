1class Solution:
2    def maxProductPath(self, grid: list[list[int]]) -> int:
3        m, n = len(grid), len(grid[0])
4        
5        max_dp = [[0]*n for _ in range(m)]
6        min_dp = [[0]*n for _ in range(m)]
7        
8        max_dp[0][0] = min_dp[0][0] = grid[0][0]
9        
10        # first column
11        for i in range(1, m):
12            max_dp[i][0] = min_dp[i][0] = max_dp[i-1][0] * grid[i][0]
13        
14        # first row
15        for j in range(1, n):
16            max_dp[0][j] = min_dp[0][j] = max_dp[0][j-1] * grid[0][j]
17        
18        for i in range(1, m):
19            for j in range(1, n):
20                val = grid[i][j]
21                
22                candidates = [
23                    max_dp[i-1][j] * val,
24                    min_dp[i-1][j] * val,
25                    max_dp[i][j-1] * val,
26                    min_dp[i][j-1] * val
27                ]
28                
29                max_dp[i][j] = max(candidates)
30                min_dp[i][j] = min(candidates)
31        
32        result = max_dp[m-1][n-1]
33        
34        if result < 0:
35            return -1
36        
37        return result % (10**9 + 7)