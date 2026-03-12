1class DSU:
2    def __init__(self, n):
3        self.p = list(range(n))
4        self.r = [0]*n
5
6    def find(self, x):
7        if self.p[x] != x:
8            self.p[x] = self.find(self.p[x])
9        return self.p[x]
10
11    def union(self, a, b):
12        ra, rb = self.find(a), self.find(b)
13        if ra == rb:
14            return False
15        if self.r[ra] < self.r[rb]:
16            ra, rb = rb, ra
17        self.p[rb] = ra
18        if self.r[ra] == self.r[rb]:
19            self.r[ra] += 1
20        return True
21
22
23class Solution:
24    def maxStability(self, n: int, edges: list[list[int]], k: int) -> int:
25
26        def can(x):
27            dsu = DSU(n)
28            used = 0
29            upgrades = 0
30
31            optional = []
32
33            # mandatory edges
34            for u, v, s, must in edges:
35                if must:
36                    if s < x:
37                        return False
38                    if not dsu.union(u, v):
39                        return False
40                    used += 1
41                else:
42                    optional.append((u, v, s))
43
44            normal = []
45            upgrade = []
46
47            for u, v, s in optional:
48                if s >= x:
49                    normal.append((u, v))
50                elif s * 2 >= x:
51                    upgrade.append((u, v))
52
53            for u, v in normal:
54                if dsu.union(u, v):
55                    used += 1
56
57            for u, v in upgrade:
58                if used == n-1:
59                    break
60                if upgrades == k:
61                    break
62                if dsu.union(u, v):
63                    upgrades += 1
64                    used += 1
65
66            return used == n-1
67
68        lo, hi = 0, max(s*2 for _,_,s,_ in edges)
69        ans = -1
70
71        while lo <= hi:
72            mid = (lo + hi) // 2
73            if can(mid):
74                ans = mid
75                lo = mid + 1
76            else:
77                hi = mid - 1
78
79        return ans