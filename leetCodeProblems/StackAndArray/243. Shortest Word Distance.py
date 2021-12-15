"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.
Example 1:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        p1 = None
        p2 = None
        size = len(wordsDict)
        ans = size
        for i in range(size):
            s = wordsDict[i]
            if s == word1:
                p1 = i
            elif s == word2:
                p2 = i

            if p1 is not None and p2 is not None:
                ans = min(ans, abs(p1 - p2))

        return ans