from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def rob_linear(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i-2], dp[i-1])
            
            return dp[-1]
        
        # Rob either from the first house to the second-last, or from the second to the last
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
