1class Solution:
2    def maxDepth(self, root) -> int:
3        if not root:
4            return 0
5
6        max_child_depth = 0
7        for child in root.children:
8            max_child_depth = max(max_child_depth, self.maxDepth(child))
9
10        return 1 + max_child_depth
11