class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        ret = 0

        for i in range(len(height)):
            if i == 0:
                left[0] = height[0]
            else:
                left[i] = max(left[i-1], height[i])
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right[len(height)-1] = height[len(height)-1]
            else:
                right[i] = max(right[i+1], height[i])
        
        for i in range(len(height)):
            ret += min(left[i], right[i]) - height[i]
        
        return ret