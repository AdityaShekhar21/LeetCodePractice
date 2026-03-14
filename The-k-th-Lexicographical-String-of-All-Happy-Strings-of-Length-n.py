1class Solution:
2    def getHappyString(self, n: int, k: int) -> str:
3        current_string = ""
4        happy_strings = []
5        # Generate all happy strings of length n
6        self.generate_happy_strings(n, current_string, happy_strings)
7
8        # Check if there are at least k happy strings
9        if len(happy_strings) < k:
10            return ""
11
12        return happy_strings[k - 1]
13
14    def generate_happy_strings(
15        self, n: int, current_string: str, happy_strings: list
16    ):
17        # If the current string has reached the desired length, add it to the list
18        if len(current_string) == n:
19            happy_strings.append(current_string)
20            return
21
22        # Try adding each character ('a', 'b', 'c') to the current string
23        for current_char in ["a", "b", "c"]:
24            # Skip if the current character is the same as the last character
25            if len(current_string) > 0 and current_string[-1] == current_char:
26                continue
27
28            # Recursively generate the next character
29            self.generate_happy_strings(
30                n, current_string + current_char, happy_strings
31            )
32