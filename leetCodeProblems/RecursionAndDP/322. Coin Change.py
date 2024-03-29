"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.
Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #         # top down solution
        #         if amount < 1:
        #             return 0

        #         def change_helper(remain, coins, seen):
        #             if remain < 0:
        #                 return -1

        #             if remain == 0:
        #                 return 0

        #             if seen[remain] != -2:
        #                 return seen[remain]

        #             MIN = float('inf')
        #             for val in coins:
        #                 res = change_helper(remain - val, coins, seen)
        #                 if res > -1 and res < MIN:
        #                     MIN = 1 + res

        #             seen[remain] = -1 if MIN == float('inf') else MIN
        #             return seen[remain]

        #         seen = [-2] * (amount + 1)
        #         return change_helper(amount, coins, seen)

        # bottom up solution
        MAX = float('inf')
        dp = [0] + [MAX] * amount

        for i in range(1, amount + 1):
            res = []
            for c in coins:
                remain = i - c
                if remain < 0:
                    res.append(MAX)
                else:
                    res.append(dp[remain])

            dp[i] = min(res) + 1

        return -1 if dp[-1] == MAX else dp[-1]