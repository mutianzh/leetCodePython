"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == None or len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        low = 0
        high = len(nums) - 1

        # Search for first position
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if nums[mid] < target:
                low = mid

            else:
                high = mid

        if nums[low] == target:
            first_index = low
        elif nums[high] == target:
            first_index = high
        else:
            return [-1, -1]

        # Search for last position
        # # Version 1: O(K)
        # left = first_index
        # while left <= len(nums)-1 and nums[left] == target:
        #     left += 1
        # return [first_index, left-1]

        # Version 2: O(log n)
        low = 0
        high = len(nums) - 1
        while low + 1 < high:
            mid = int(low + (high - low) / 2)
            if nums[mid] > target:
                high = mid

            else:
                low = mid

        if nums[high] == target:
            last_index = high
        elif nums[low] == target:
            last_index = low
        else:
            return [-1, -1]

        return [first_index, last_index]
