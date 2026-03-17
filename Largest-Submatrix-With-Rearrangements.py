1class Solution:
2    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
3        m, n = len(matrix), len(matrix[0])
4        
5        # Step 1: Build heights
6        for i in range(1, m):
7            for j in range(n):
8                if matrix[i][j] == 1:
9                    matrix[i][j] += matrix[i-1][j]
10        
11        max_area = 0
12        
13        # Step 2: Process each row
14        for row in matrix:
15            row.sort(reverse=True)
16            
17            for j in range(n):
18                area = row[j] * (j + 1)
19                max_area = max(max_area, area)
20        
21        return max_area