class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [999] * len(nums)
        dp[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            jump = nums[i]
            for j in range(i, min(i+jump+1, len(nums))):
                if dp[j] != 999:
                    dp[i] = min(dp[i], 1+dp[j])
        
        return dp[0]
