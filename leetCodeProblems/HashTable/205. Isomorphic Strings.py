"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.
Example 1:
Input: s = "egg", t = "add"
Output: true
Example 2:
Input: s = "foo", t = "bar"
Output: false
Example 3:
Input: s = "paper", t = "title"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace = {}
        seen = set()

        len_1 = len(s)
        len_2 = len(t)

        if len_1 != len_2:
            return False

        for i in range(len_1):
            c_1 = s[i]
            c_2 = t[i]

            if c_1 not in replace:
                if c_2 not in seen:
                    replace[c_1] = c_2
                    seen.add(c_2)
                else:
                    return False

            else:
                c_r = replace[c_1]
                if c_r != c_2:
                    return False

        return True
