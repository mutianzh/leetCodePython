"""
Given a string s, return the longest palindromic substring in s.
Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

import copy
class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s or len(s) == 0:
            return s

        ans = ""
        for i in range(len(s)):
            # odd case
            ans = self.helper(i, i, ans, s)

            # even case
            ans = self.helper(i, i + 1, ans, s)

        return ans

    def helper(self, i, j, ans, s):
        temp = ""
        while i >= 0 and j < len(s) and s[i] == s[j]:
            temp = s[i:j + 1]
            i -= 1
            j += 1

        if len(temp) > len(ans):
            ans = copy.deepcopy(temp)

        return ans