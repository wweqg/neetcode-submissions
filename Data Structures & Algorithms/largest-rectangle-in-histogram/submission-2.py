class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            while s and s[-1][-1] > h:
                ii, ih = s.pop()
                res = max(res, ih * (i - ii))
                start = ii
            s.append((start, h))
        
        for i, h in s:
            res = max(res, h * (len(heights) - i))
        
        return res