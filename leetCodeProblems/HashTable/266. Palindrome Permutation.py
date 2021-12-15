"""
Given a string s, return true if a permutation of the string could form a palindrome.
Example 1:
Input: s = "code"
Output: false
Example 2:
Input: s = "aab"
Output: true
Example 3:
Input: s = "carerac"
Output: true
"""
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd_count = 0
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
            if count[c] % 2 > 0:
                odd_count += 1
            else:
                odd_count -= 1

        return False if odd_count > 1 else True
