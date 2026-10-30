from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx, n in enumerate(nums):
            if idx > 0 and n == nums[idx - 1]:
                continue  # Skip duplicates for the first element
            
            i = idx + 1
            j = len(nums) - 1
            while i < j:
                total = n + nums[i] + nums[j]
                if total > 0:
                    j -= 1
                elif total < 0:
                    i += 1
                else:
                    res.append([n, nums[i], nums[j]])
                    
                    # Move i and j to the next different elements to avoid duplicates
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    
                    i += 1
                    j -= 1
        
        return res
