"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...
Example 1:
Input: columnNumber = 1
Output: "A"
Example 2:
Input: columnNumber = 28
Output: "AB"
Example 3:
Input: columnNumber = 701
Output: "ZY"
Example 4:
Input: columnNumber = 2147483647
Output: "FXSHRXW"
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        ans = ""
        while n > 0:
            n -= 1
            r = n % 26
            n = int(n / 26)
            c = chr(ord('A') + r)
            ans += c

        return ans[::-1]