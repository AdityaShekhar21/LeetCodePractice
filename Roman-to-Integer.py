1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {
4            'I': 1,
5            'V': 5,
6            'X': 10,
7            'L': 50,
8            'C': 100,
9            'D': 500,
10            'M': 1000
11        }
12
13        total = 0
14        prev = 0
15
16        for ch in reversed(s):
17            value = roman[ch]
18            if value < prev:
19                total -= value
20            else:
21                total += value
22            prev = value
23
24        return total
25