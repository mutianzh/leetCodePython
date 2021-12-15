"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:
Input: pattern = "abba", s = "dog dog dog dog"
Output: false
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        n = len(pattern)
        mapping = {}
        seen = set()
        for i in range(n):
            c = pattern[i]
            word = words[i]
            if c in mapping:
                map_word = mapping[c]
                if map_word != word:
                    return False
            else:
                if word in seen:
                    return False

                mapping[c] = word
                seen.add(word)

        return True



