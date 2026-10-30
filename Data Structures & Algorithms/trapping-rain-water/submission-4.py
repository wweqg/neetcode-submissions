class Solution:
    def trap(self, height: List[int]) -> int:

        maxLeft = [float('-inf')] * len(height)
        maxRight = [float('-inf')] * len(height)
        maxLeft[0] = height[0]
        for i in range(1, len(height), 1):
            maxLeft[i] = max(height[i], maxLeft[i-1])
        maxRight[-1] = height[-1]
        for i in range(len(height)-2, -1, -1):
            maxRight[i] = max(height[i], maxRight[i+1])
        
        res = 0
        for i in range(len(height)):
            tmp = min(maxLeft[i], maxRight[i]) - height[i]
            res += tmp
        
        return res
         