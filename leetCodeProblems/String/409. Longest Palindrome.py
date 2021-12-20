"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.
Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
Input: s = "a"
Output: 1
Example 3:
Input: s = "bb"
Output: 2
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        num_odds = sum([freq % 2 for _, freq in counts.items()])

        return len(s) if num_odds <= 1 else len(s) - num_odds + 1
