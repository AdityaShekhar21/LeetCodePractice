1class Solution:
2    def reverseSubmatrix(
3        self, grid: List[List[int]], x: int, y: int, k: int
4    ) -> List[List[int]]:
5        i0, i1 = x, x + k - 1
6        while i0 < i1:
7            for j in range(y, y + k):
8                grid[i0][j], grid[i1][j] = grid[i1][j], grid[i0][j]
9            i0, i1 = i0 + 1, i1 - 1
10        return grid