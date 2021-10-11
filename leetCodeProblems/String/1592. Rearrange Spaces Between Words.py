"""
Example 1:

Input: text = "  this   is  a sentence "
Output: "this   is   a   sentence"
Explanation: There are a total of 9 spaces and 4 words. We can evenly divide the 9 spaces between the words: 9 / (4-1) = 3 spaces.
Example 2:

Input: text = " practice   makes   perfect"
Output: "practice   makes   perfect "
Explanation: There are a total of 7 spaces and 3 words. 7 / (3-1) = 3 spaces plus 1 extra space. We place this extra space at the end of the string.
Example 3:

Input: text = "hello   world"
Output: "hello   world"
Example 4:

Input: text = "  walks  udp package   into  bar a"
Output: "walks  udp  package  into  bar  a "
Example 5:

Input: text = "a"
Output: "a"
"""


class Solution(object):

    def reorderSpaces(self, text):
        words = text.split()
        num_words = len(words)
        num_spaces = text.count(' ')
        if num_words == 1:
            avg = 0
        else:
            avg = num_spaces // (num_words - 1)

        tailing_spaces = num_spaces - avg * (num_words - 1)

        return (' ' * avg).join(words) + ' ' * tailing_spaces