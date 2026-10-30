class Solution:
    def jump(self, nums: List[int]) -> int:
        step = [float('inf')] * len(nums)
        step[-1] = 0

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                step[i] = min(step[i], 1+step[j])
        
        return step[0]