class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for idx, i in enumerate(nums):
            if (target-i) in m:
                return [m[target-i], idx]
            m[i] = idx
        
        return []