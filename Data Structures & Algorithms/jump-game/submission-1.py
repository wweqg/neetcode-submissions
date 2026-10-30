class Solution:
    def canJump(self, nums: List[int]) -> bool:
        can = [False] * len(nums)
        can[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                can[i] = can[i] or can[j]
        
        return can[0]