"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, left, right):
            if len(path) == 2 * n:
                ans.append("".join(path))

            if left < n:
                path.append("(")
                backtrack(path, left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(path, left, right + 1)
                path.pop()

        ans = []
        backtrack([], 0, 0)
        return ans