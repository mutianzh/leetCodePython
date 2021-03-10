"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Input: s = "()[]{}"
Output: true

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = dict()
        mapping['}'] = '{'
        mapping[')'] = '('
        mapping[']'] = '['
        for elem in s:
            if elem == '{' or elem == '(' or elem == '[':
                stack.append(elem)

            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == mapping[elem]:
                        stack = stack[:-1]
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False