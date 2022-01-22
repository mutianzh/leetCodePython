"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return None

        p0 = 0  # border for zeros
        p1 = 0
        p2 = len(nums) - 1  # border for 2s

        while p1 <= p2:
            v = nums[p1]
            if v == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                # we can add 1 to p1 because p0 must point at 1 since if it is two it will be swapped with p2
                p0 += 1
                p1 += 1

            elif v == 1:
                p1 += 1

            else:
                nums[p2], nums[p1] = nums[p1], nums[p2]
                p2 -= 1

        return nums