class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()
        res = 0

        for n in nums:
            hs.add(n)

        for n in hs:
            curr = n
            count = 1
            while curr + 1 in hs:
                curr = curr + 1
                count += 1 
            res = max(count, res)
        
        return res