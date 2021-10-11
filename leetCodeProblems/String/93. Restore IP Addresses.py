"""
Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:

Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:

Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def output(pos):
            segment = s[pos + 1:]  # The remaining segment after the last dot
            if valid(segment):
                segments.append(segment)
                ans.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos, dots_left):
            # pos means the dot is placed behind s[pos]
            # Dot can not be placed behind the last char, so pos ranges from
            # prev_pos + 1 to n-2 or prev_pos + 3
            for pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1: pos + 1]
                if valid(segment):
                    segments.append(segment)  # record current segment next place the next dot
                    if dots_left - 1 == 0:
                        # This is already the last dot
                        output(pos)
                    else:
                        # Place the next dot
                        backtrack(pos, dots_left - 1)

                    segments.pop()  # pop out the last segment for backtracking

        segments = []
        ans = []
        n = len(s)
        backtrack(-1, 3)
        return ans

solution = Solution()

s = "25525511135"
print(solution.restoreIpAddresses(s))