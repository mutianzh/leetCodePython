"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(path, num, result):
            if not num:
                result.append(path)
                return

            seen = set()
            for i in range(len(num)):
                v = num[i]
                if v not in seen:
                    seen.add(v)
                    dfs(path + [v], num[:i] + num[i + 1:], result)

        dfs([], nums, result)

        return result

