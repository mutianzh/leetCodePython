"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version.
You should minimize the number of calls to the API.

"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import math

def isBadVersion(n):
    bad = 2
    if int(n) >= bad:
        return True
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            if isBadVersion(1):
                return 1
            else:
                return 2
        else:
            low = 1
            high = n

            # # Version 1
            # while low <= high:
            #
            #     mid = math.floor((low + high) / 2)
            #     if isBadVersion(mid):
            #         high = mid - 1
            #     else:
            #         low = mid + 1
            #
            # if isBadVersion(mid):
            #     return int(mid)
            # else:
            #     return int(mid + 1)
            #
            # return int(mid)

            # Version 2
            while low + 1 < high:
                mid = math.floor((low + high) / 2)
                if isBadVersion(mid):
                    high = mid
                else:
                    low = mid

            if isBadVersion(low):
                return int(low)
            else:
                return int(high)




solution = Solution()
print(solution.firstBadVersion(3))
