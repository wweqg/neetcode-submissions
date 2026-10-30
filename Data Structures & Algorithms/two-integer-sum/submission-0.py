class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, n in enumerate(nums):
            tmp = target - n
            if tmp in hm:
                return [hm[tmp], i]
            else:
                hm[n] = i
        
        return [-1, -1]