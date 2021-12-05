"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.
Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def patition(nums, left, right, index):
            if left == right:
                return left

            # swap pivot with right most element
            nums[index], nums[right] = nums[right], nums[index]

            store_index = left
            for i in range(left, right):
                if nums[i] < nums[right]:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1

            # swap pivot to store_index
            nums[store_index], nums[right] = nums[right], nums[store_index]

            return store_index

        def quick_select(nums, left, right, good_location):

            if left == right:
                return

            pivot = random.randrange(left, right)

            pivot = patition(nums, left, right, pivot)
            if pivot == good_location:
                return
            elif pivot < good_location:
                # quick select on right side
                quick_select(nums, pivot + 1, right, good_location)
            else:
                quick_select(nums, left, pivot - 1, good_location)

            return

        if not nums or len(nums) < k:
            return -1
        n = len(nums)
        quick_select(nums, 0, n - 1, n - k)
        return nums[-k]