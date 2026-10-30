class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0
        for n in nums:
            curr += n
            res = max(res, curr)
            curr = max(0, curr)
        
        return res