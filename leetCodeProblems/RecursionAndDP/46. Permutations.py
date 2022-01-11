"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        n = len(nums)

        # sol 1: dfs
        def dfs(path, remain, result):
            if not remain:
                result.append(path)

            for i in range(len(remain)):
                dfs(path + [remain[i]], remain[:i] + remain[i + 1:], result)

        dfs([], nums, result)

        return result