"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
Example 1:
Input: num = 16
Output: true
Example 2:
Input: num = 14
Output: false
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False