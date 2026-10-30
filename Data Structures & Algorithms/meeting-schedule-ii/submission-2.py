"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        start = sorted(intervals, key=lambda x: x.start)
        end = sorted(intervals, key=lambda x: x.end)

        sp = 0
        ep = 0

        n = len(intervals)
        count = 0
        res = float('-inf')

        while sp < n and ep < n:
            if start[sp].start < end[ep].end:
                count += 1
                sp += 1
                res = max(count, res)
            else:
                count -= 1
                ep += 1
        
        return res