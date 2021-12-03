"""
198. House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
import numpy

class Solution(object):

    #     # Recursion solution
    #     def __init__(self):
    #         self.memo = {}

    #     def rob(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         if nums:
    #             if len(nums) == 0:
    #                 return 0
    #             elif len(nums) == 1:
    #                 return nums[0]
    #             else:
    #                 self.memo = {}
    #                 return self.robFrom(0, nums)
    #         else:
    #             return -1

    #     def robFrom(self, i, nums):
    #         if i > len(nums) - 1:
    #             return 0
    #         else:
    #             if i in self.memo:
    #                 return self.memo[i]
    #             else:
    #                 result = max(nums[i] + self.robFrom(i+2, nums), self.robFrom(i+1, nums))
    #                 self.memo[i] = result
    #                 return result

    # DP solution

    def rob(self, nums):

        if nums:
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                N = len(nums)
                robFrom = [None] * (N + 1)
                robFrom[N] = 0  # No house to rob from
                robFrom[N - 1] = nums[N - 1]
                for i in range(N - 2, -1, -1):
                    robFrom[i] = max(nums[i] + robFrom[i + 2], robFrom[i + 1])

            return robFrom[0]

        else:
            return -1

def rob(nums):
    #         if nums:
    #             if len(nums) == 0:
    #                 return 0
    #             elif len(nums) == 1:
    #                 return nums[0]
    #             else:
    #                 N = len(nums)
    #                 robFrom = [None] * (N + 1)
    #                 robFrom[N] = 0 # No house to rob from
    #                 robFrom[N - 1] = nums[N - 1]
    #                 for i in range(N-2, -1, -1):
    #                     robFrom[i] = max(nums[i] + robFrom[i+2], robFrom[i+1])

    #             return robFrom[0]

    #         else:
    #             return -1

    # if nums:
    #     if len(nums) <= 1:
    #         return numpy.sum(nums)
    #     else:
    #         N = len(nums)
    #         robFrom = [0] * (N + 1)
    #         robFrom[N] = 0
    #         robFrom[0] = nums[0]
    #         for i in range(1, len(nums)):
    #             robFrom[i] = max(nums[i] + robFrom[i - 2], robFrom[i - 1])
    #
    #         return robFrom[N - 1]
    # else:
    #     return 0

    if not nums or len(nums) == 0:
        return 0

    N = len(nums)
    rob_prev_prev = 0
    rob_prev = nums[0]
    for i in range(1, N):
        curr = max(rob_prev_prev + nums[i], rob_prev)

        rob_prev_prev = rob_prev
        rob_prev = curr

    return rob_prev