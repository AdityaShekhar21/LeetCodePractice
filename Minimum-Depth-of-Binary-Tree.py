1from collections import deque
2
3class Solution:
4    def minDepth(self, root) -> int:
5        if not root:
6            return 0
7
8        queue = deque([(root, 1)])
9
10        while queue:
11            node, depth = queue.popleft()
12            
13            if not node.left and not node.right:
14                return depth
15
16            if node.left:
17                queue.append((node.left, depth + 1))
18            if node.right:
19                queue.append((node.right, depth + 1))
20