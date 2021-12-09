"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1

        # when while loop finishes
        # r < l
        # nums[r] < target < nums[l]

        return l