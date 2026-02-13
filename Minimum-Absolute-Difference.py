1class Solution:
2    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
3        arr.sort()
4        
5        min_diff = float('inf')
6        result = []
7
8        for i in range(1, len(arr)):
9            diff = arr[i] - arr[i-1]
10            min_diff = min(min_diff, diff)
11
12        for i in range(1, len(arr)):
13            if arr[i] - arr[i-1] == min_diff:
14                result.append([arr[i-1], arr[i]])
15
16        return result
17