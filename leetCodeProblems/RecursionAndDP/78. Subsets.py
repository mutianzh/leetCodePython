"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(start, curr):
            if len(curr) == k:
                output.append(list(curr))
                return

            for i in range(start, n):
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        n = len(nums)
        output = []
        for k in range(n + 1):
            backtrack(0, [])

        return output
