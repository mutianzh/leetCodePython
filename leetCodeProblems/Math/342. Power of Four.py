"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
Example 1:
Input: n = 16
Output: true
Example 2:
Input: n = 5
Output: false
Example 3:
Input: n = 1
Output: true
"""
import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #         # brute force
        #         if n <= 0:
        #             return False

        #         while n % 4 == 0:
        #             n /= 4

        #         return n == 1

        # math: check if log2(x) is an even number
        return n > 0 and math.log2(n) % 2 == 0