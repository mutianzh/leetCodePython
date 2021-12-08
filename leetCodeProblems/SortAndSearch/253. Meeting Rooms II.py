"""
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.
Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
"""


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        start_time = sorted([x[0] for x in intervals])
        end_time = sorted([x[1] for x in intervals])

        index_1 = 0  # index for start time
        index_2 = 0  # index for end time
        num_meets = len(intervals)
        num_room = 0

        while index_1 < num_meets:
            if start_time[index_1] < end_time[index_2]:
                num_room += 1
            else:
                index_2 += 1

            index_1 += 1

        return num_room