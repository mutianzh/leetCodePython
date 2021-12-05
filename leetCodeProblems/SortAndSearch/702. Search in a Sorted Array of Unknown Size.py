"""
This is an interactive problem.

You have a sorted array of unique elements and an unknown size. You do not have an access to the array but you can use the ArrayReader interface to access it. You can call ArrayReader.get(i) that:

returns the value at the ith index (0-indexed) of the secret array (i.e., secret[i]), or
returns 231 - 1 if the i is out of the boundary of the array.
You are also given an integer target.

Return the index k of the hidden array where secret[k] == target or return -1 otherwise.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: secret = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in secret and its index is 4.
Example 2:

Input: secret = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in secret so return -1.
"""


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """

        no_value = 2 ** 31 - 1
        if reader.get(0) == no_value:
            return -1

        left = 0
        right = 1
        r_value = reader.get(right)
        while r_value < target and r_value != no_value:
            left = right
            right *= 2
            r_value = reader.get(right)

        # perform binary search between left and right index
        while left <= right:
            mid = left + (right - left) // 2
            mid_value = reader.get(mid)
            if mid_value == target:
                return mid
            elif mid_value == no_value or mid_value > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1