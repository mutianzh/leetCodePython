"""
Given a sorted (in ascending order) integer array nums of n elements and a target value,
write a function to search target in nums. If target exists, then return its index, otherwise return -1.
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0 or nums == None:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        low = 0
        high = len(nums) - 1

        # # Version 1
        # while low <= high:
        #     mid = int((low + high) / 2)
        #     if nums[mid] == target:
        #         return mid
        #
        #     elif nums[mid] > target:
        #         high = mid - 1
        #
        #     else:
        #         low = mid + 1
        #
        # return -1

        # Version 2
        while low + 1 < high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                high = mid

            else:
                low = mid

        if nums[low] == target:
            return low
        if nums[high] == target:
            return high
        return -1
