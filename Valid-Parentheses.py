1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        mapping = {')': '(', '}': '{', ']': '['}
5
6        for ch in s:
7            if ch in mapping:
8                if not stack or stack[-1] != mapping[ch]:
9                    return False
10                stack.pop()
11            else:
12                stack.append(ch)
13
14        return not stack
15