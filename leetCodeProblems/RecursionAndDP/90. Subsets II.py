"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:
Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, start):
            if len(path) == k:
                result.append(list(path))
                return

            seen = set()
            for i in range(start, len(nums)):
                v = nums[i]
                if v in seen:
                    continue
                else:
                    seen.add(v)
                    path.append(v)
                    backtrack(path, i + 1)
                    path.pop()

        nums.sort()
        result = []
        for k in range(0, len(nums) + 1):
            backtrack([], 0)

        return result