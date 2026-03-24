1class Solution:
2    def constructProductMatrix(self, grid: list[list[int]]) -> list[list[int]]:
3        MOD = 12345
4        n, m = len(grid), len(grid[0])
5        
6        # Step 1: Flatten
7        arr = []
8        for row in grid:
9            arr.extend(row)
10        
11        size = len(arr)
12        
13        # Step 2: Prefix
14        prefix = [1]*size
15        for i in range(1, size):
16            prefix[i] = (prefix[i-1] * arr[i-1]) % MOD
17        
18        # Step 3: Suffix
19        suffix = [1]*size
20        for i in range(size-2, -1, -1):
21            suffix[i] = (suffix[i+1] * arr[i+1]) % MOD
22        
23        # Step 4: Build result
24        res = [0]*size
25        for i in range(size):
26            res[i] = (prefix[i] * suffix[i]) % MOD
27        
28        # Step 5: Convert back to matrix
29        ans = []
30        idx = 0
31        for i in range(n):
32            row = []
33            for j in range(m):
34                row.append(res[idx])
35                idx += 1
36            ans.append(row)
37        
38        return ans