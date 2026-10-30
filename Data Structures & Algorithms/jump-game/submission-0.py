class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums)-2, -1, -1):
            jump = nums[i]
            for j in range(i, min(i+jump+1, len(nums))):
                dp[i] = dp[i] or dp[j]

        return dp[0]