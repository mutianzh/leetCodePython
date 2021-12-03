"""
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        #         # Solution 1: backtrack with counters

        #         counter = Counter(candidates)
        #         counter = [(n, counter[n]) for n in counter]
        #         results = []

        #         def backtrack(remain, comb, results, counter, start):
        #             if remain == 0:
        #                 results.append(list(comb))
        #                 return
        #             elif remain < 0:
        #                 return

        #             for i in range(start, len(counter)):
        #                 n, freq = counter[i]
        #                 if freq <= 0:
        #                     continue

        #                 comb.append(n)
        #                 counter[i] = (n, freq - 1)
        #                 backtrack(remain - n, comb, results, counter, i)

        #                 counter[i] = (n, freq)
        #                 comb.pop()

        #         backtrack(target, [], results, counter, 0)
        #         return results

        # Solution 2: backtrack with index
        results = []
        candidates.sort()
        def backtrack(remain, comb, results, start):
            if remain == 0:
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[ i -1]:
                    continue

                comb.append(candidates[i])
                backtrack(remain - candidates[i], comb, results, i+ 1)
                comb.pop()

        backtrack(target, [], results, 0)
        return results
