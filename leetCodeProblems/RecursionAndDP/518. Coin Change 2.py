"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
You may assume that you have an infinite number of each kind of coin.
The answer is guaranteed to fit into a signed 32-bit integer.
Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
"""


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount < 1:
            return 1

        if len(coins) < 1:
            return 0

        #         # top down approach
        #         def find_change(remain, index, coins, seen):
        #             if index == len(coins) - 1:
        #                 if remain % coins[index] == 0:
        #                     return 1
        #                 else:
        #                     return 0

        #             if seen[remain][index] > -1:
        #                 return seen[remain][index]

        #             i = 0
        #             ways = 0
        #             value = coins[index]
        #             while i * value <= remain:
        #                 ways += find_change(remain - i * value, index + 1, coins, seen)
        #                 i += 1

        #             seen[remain][index] = ways
        #             return seen[remain][index]

        #         seen = [[-1 for c in coins] for i in range(amount + 1)]
        #         return find_change(amount, 0, coins, seen)

        # bottom up approach

        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for m in range(1, amount + 1, 1):
                remain = m - c
                if remain >= 0:
                    dp[m] += dp[remain]

        return dp[amount]