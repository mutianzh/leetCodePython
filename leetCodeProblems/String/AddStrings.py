"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mapping = dict()
        mapping['0'] = 0
        mapping['1'] = 1
        mapping['2'] = 2
        mapping['3'] = 3
        mapping['4'] = 4
        mapping['5'] = 5
        mapping['6'] = 6
        mapping['7'] = 7
        mapping['8'] = 8
        mapping['9'] = 9

        res = []
        carry = 0

        num1_array = []
        num2_array = []

        len1 = len(num1)
        len2 = len(num2)
        max_len = max(len1, len2)

        for i in range(-1, -max_len - 1, -1):
            if i >= -len1 and i >= -len2:
                digit1 = mapping[num1[i]]
                digit2 = mapping[num2[i]]
                value = digit1 + digit2 + carry
                digit = value % 10
                carry = value // 10
                res.append(digit)
            elif i < -len1:
                value = mapping[num2[i]] + carry
                digit = value % 10
                carry = value // 10
                res.append(digit)
            elif i < -len2:
                value = mapping[num1[i]] + carry
                digit = value % 10
                carry = value // 10
                res.append(digit)

        if carry > 0:
            res.append(carry)
        s = ""
        for item in res[::-1]:
            s += "%s" % item

        return s