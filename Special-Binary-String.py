1class Solution:
2    def makeLargestSpecial(self, s: str) -> str:
3        count = 0
4        start = 0
5        blocks = []
6
7        for i, ch in enumerate(s):
8            if ch == '1':
9                count += 1
10            else:
11                count -= 1
12
13            # found a special substring
14            if count == 0:
15                inner = s[start+1:i]
16                # recursively optimize inside
17                blocks.append("1" + self.makeLargestSpecial(inner) + "0")
18                start = i + 1
19
20        # sort descending for lexicographically largest
21        blocks.sort(reverse=True)
22        return "".join(blocks)