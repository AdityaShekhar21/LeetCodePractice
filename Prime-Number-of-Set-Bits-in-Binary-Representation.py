1class Solution:
2    def countPrimeSetBits(self, left: int, right: int) -> int:
3        primes = {2, 3, 5, 7, 11, 13, 17, 19}
4        count = 0
5
6        for num in range(left, right + 1):
7            bits = num.bit_count()   # fast built-in bit count
8            if bits in primes:
9                count += 1
10
11        return count