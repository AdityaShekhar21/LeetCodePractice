1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        seen = set()
4        left = 0
5        max_len = 0
6
7        for right in range(len(s)):
8            while s[right] in seen:
9                seen.remove(s[left])
10                left += 1
11
12            seen.add(s[right])
13            max_len = max(max_len, right - left + 1)
14
15        return max_len
16