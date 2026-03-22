1class Solution:
2    def findRotation(
3        self, mat: List[List[int]], target: List[List[int]]
4    ) -> bool:
5        n = len(mat)
6        # at most 4 rotations
7        for k in range(4):
8            # rotation operation
9            for i in range(n // 2):
10                for j in range((n + 1) // 2):
11                    (
12                        mat[i][j],
13                        mat[n - 1 - j][i],
14                        mat[n - 1 - i][n - 1 - j],
15                        mat[j][n - 1 - i],
16                    ) = (
17                        mat[n - 1 - j][i],
18                        mat[n - 1 - i][n - 1 - j],
19                        mat[j][n - 1 - i],
20                        mat[i][j],
21                    )
22
23            if mat == target:
24                return True
25        return False