"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
"""

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s or not t:
            return False

        if len(s) != len(t):
            return False

        count_s = collections.defaultdict(int)
        count_t = collections.defaultdict(int)
        for c in s:
            count_s[c] += 1

        for c in t:
            count_t[c] += 1

        for c in count_s.keys():
            if count_s[c] != count_t[c]:
                return False

        return True