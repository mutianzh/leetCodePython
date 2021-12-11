"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
Example 1:
Input: nums = [2,2,1]
Output: 1
Example 2:
Input: nums = [4,1,2,1,2]
Output: 4
Example 3:
Input: nums = [1]
Output: 1
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # sol 1: hash table
        seen = set()
        candidates = set()
        for num in nums:
            if num in seen:
                candidates.remove(num)
            else:
                candidates.add(num)
                seen.add(num)

        return candidates.pop()

        # # sol 2: math
        # return 2 * sum(set(nums)) - sum(nums)