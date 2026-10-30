class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = [[] for _ in range(len(nums) + 1)] # count[i] = []
        d = {}
        ans = []
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        for key,val in d.items():
            arr = countArr[val] 
            arr.append(key)
        
        for freq in range(len(nums), 0, -1):
            for f in countArr[freq]:
                ans.append(f)
                if len(ans) == k:
                    return ans

        return None
            

        