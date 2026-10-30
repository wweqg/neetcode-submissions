class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ret = 0

        while l < r:
            width = r - l
            if heights[l] <= heights[r]:
                ret = max(ret, width * heights[l])
                l += 1
            else:
                ret = max(ret, width * heights[r])
                r -= 1
        
        return ret