class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        res = float('-inf')
        while i < j:
            if heights[i] > heights[j]:
                tmp = heights[j] * (j-i)
                res = max(res, tmp)
                j -= 1
            else:
                tmp = heights[i] * (j-i)
                res=max(res, tmp)
                i += 1
        
        return res