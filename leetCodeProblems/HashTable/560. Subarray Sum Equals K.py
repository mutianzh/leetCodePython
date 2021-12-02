"""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
"""

import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = collections.defaultdict(int)
        sum = 0
        count = 0
        for num in nums:
            sum += num

            if sum == k:
                count += 1

            count += h[sum - k]

            h[sum] += 1

        return count