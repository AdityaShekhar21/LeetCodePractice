1class Solution:
2    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
3        if not matrix or not matrix[0]:
4            return False
5
6        m, n = len(matrix), len(matrix[0])
7        left, right = 0, m * n - 1
8
9        while left <= right:
10            mid = (left + right) // 2
11            row = mid // n
12            col = mid % n
13
14            if matrix[row][col] == target:
15                return True
16            elif matrix[row][col] < target:
17                left = mid + 1
18            else:
19                right = mid - 1
20
21        return False
22