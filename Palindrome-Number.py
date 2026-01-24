1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        if x<0:
4            return False
5        s = str(x)
6        return s == s[::-1]
7        