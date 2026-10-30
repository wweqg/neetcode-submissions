class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for n in nums:
            if n not in hm:
                hm[n] = 0
            hm[n] += 1
        
        tmp = [[] for _ in range(len(nums) + 1)] 

        for key, value in hm.items():
            tmp[value].append(key)
        
        res = []
        for i in range(len(tmp)-1, -1, -1):
            for num in tmp[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res

