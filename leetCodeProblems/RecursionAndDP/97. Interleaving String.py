"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:
s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.
Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l3 != l1 + l2:
            return False

        # dp[i][j] represents if s1[: i] and s2[: j] and form s3[: i + j]

        dp = [[True for _ in range(l2 + 1)] for _ in range(l1 + 1)]

        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True

                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[j - 1]

                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i - 1]

                else:
                    # where should we get the i + j th character x in s3?
                    # choice 1: Try to get x from s1, before checking that, s1[:i - 1] and s2[:j] should be able to form
                    # s3[:i + j], which means dp[i - 1][j] should be true
                    cond1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]

                    # Get the character from s2, which requires dp[i][j - 1] to be true
                    cond2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                    dp[i][j] = cond1 or cond2

        return dp[l1][l2]
