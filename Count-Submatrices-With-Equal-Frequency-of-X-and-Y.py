1class Solution:
2    def numberOfSubmatrices(self, grid: list[list[str]]) -> int:
3        m, n = len(grid), len(grid[0])
4        
5        # Convert grid
6        val = [[0]*n for _ in range(m)]
7        hasX = [[0]*n for _ in range(m)]
8        
9        for i in range(m):
10            for j in range(n):
11                if grid[i][j] == 'X':
12                    val[i][j] = 1
13                    hasX[i][j] = 1
14                elif grid[i][j] == 'Y':
15                    val[i][j] = -1
16        
17        # Prefix sums
18        for i in range(m):
19            for j in range(n):
20                if i > 0:
21                    val[i][j] += val[i-1][j]
22                    hasX[i][j] += hasX[i-1][j]
23                if j > 0:
24                    val[i][j] += val[i][j-1]
25                    hasX[i][j] += hasX[i][j-1]
26                if i > 0 and j > 0:
27                    val[i][j] -= val[i-1][j-1]
28                    hasX[i][j] -= hasX[i-1][j-1]
29        
30        result = 0
31        
32        for i in range(m):
33            for j in range(n):
34                if val[i][j] == 0 and hasX[i][j] > 0:
35                    result += 1
36        
37        return result