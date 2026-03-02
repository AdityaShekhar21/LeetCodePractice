1class Solution:
2    def minSwaps(self, grid: list[list[int]]) -> int:
3        n = len(grid)
4        trailing_zeros = []
5
6        # Step 1: Count trailing zeros for each row
7        for row in grid:
8            count = 0
9            for val in reversed(row):
10                if val == 0:
11                    count += 1
12                else:
13                    break
14            trailing_zeros.append(count)
15
16        swaps = 0
17
18        # Step 2: Try to place rows greedily
19        for i in range(n):
20            needed = n - i - 1
21            j = i
22
23            # Find row with enough trailing zeros
24            while j < n and trailing_zeros[j] < needed:
25                j += 1
26
27            if j == n:
28                return -1
29
30            # Bubble it up
31            while j > i:
32                trailing_zeros[j], trailing_zeros[j - 1] = (
33                    trailing_zeros[j - 1],
34                    trailing_zeros[j],
35                )
36                swaps += 1
37                j -= 1
38
39        return swaps