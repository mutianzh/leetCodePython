"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # approach 1
        # n = len(s)
        # left = 0
        # right = n - 1
        # while left <= right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        # approach 2
        s.reverse()