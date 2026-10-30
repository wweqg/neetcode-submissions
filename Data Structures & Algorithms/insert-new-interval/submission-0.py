class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newi = newInterval
        intervals.sort()
        res = []

        for i in intervals:
            if i[1] < newi[0]:
                res.append(i)
                continue
            if newi[1] < i[0]:
                res.append(newi)
                newi = i
                continue
            newi[0] = min(newi[0], i[0])
            newi[1] = max(newi[1], i[1])

        res.append(newi)

        return res 