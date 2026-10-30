class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = []
        curr = intervals[0]

        for i in range(1, len(intervals)):
            i = intervals[i]
            if curr[1] < i[0]:
                res.append(curr)
                curr = i
            else:
                curr[1] = max(i[1], curr[1])
        
        res.append(curr)

        return res
            