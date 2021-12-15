"""
Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        size = len(intervals)
        for i in range(size - 1):
            cur_meet = intervals[i]
            next_meet = intervals[i + 1]
            if cur_meet[1] > next_meet[0]:
                return False

        return True
