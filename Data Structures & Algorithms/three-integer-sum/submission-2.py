class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ret = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -(nums[i])
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[j] + nums[k]) < target:
                    j += 1
                elif (nums[j] + nums[k]) > target:
                    k -= 1
                else:
                    ret.append([nums[i], nums[j], nums[k]])
                    
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
        
        return ret