1class Solution:
2    def maxDepth(self, root) -> int:
3        if not root:
4            return 0
5        
6        left_depth = self.maxDepth(root.left)
7        right_depth = self.maxDepth(root.right)
8        
9        return 1 + max(left_depth, right_depth)
10