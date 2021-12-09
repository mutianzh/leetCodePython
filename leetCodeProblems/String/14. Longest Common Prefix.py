"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not string:
            return ""

        first_str = strs[0]
        length = len(first_str)
        prefix = ""
        for i in range(length):
            c = first_str[i]

            for s in strs:
                if i >= len(s) or c != s[i]:
                    return prefix

            prefix += c

        return prefix