class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x: x[0])
        prev = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < prev:
                res += 1
                prev = min(curr[1], prev)
            else:
                prev = curr[1]
        
        return res