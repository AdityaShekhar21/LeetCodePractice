1class Solution:
2    def balanceBST(self, root):
3        nodes = []
4
5        def inorder(node):
6            if not node:
7                return
8            inorder(node.left)
9            nodes.append(node)
10            inorder(node.right)
11
12        def build(left, right):
13            if left > right:
14                return None
15
16            mid = (left + right) // 2
17            root = nodes[mid]
18            root.left = build(left, mid - 1)
19            root.right = build(mid + 1, right)
20            return root
21
22        inorder(root)
23        return build(0, len(nodes) - 1)
24