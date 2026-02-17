1class Solution:
2    def readBinaryWatch(self, turnedOn: int) -> list[str]:
3        result = []
4
5        for hour in range(12):
6            for minute in range(60):
7                if (bin(hour).count('1') + bin(minute).count('1')) == turnedOn:
8                    result.append(f"{hour}:{minute:02d}")
9
10        return result
11