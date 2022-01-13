"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion.
Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        # step 1: put new interval into the position
        p = 0
        start = newInterval[0]
        for interval in intervals:
            if start > interval[0]:
                p += 1
            else:
                break

        intervals.insert(p, newInterval)

        # step 2: merge mergable intervals
        merged = []
        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1])

        return merged