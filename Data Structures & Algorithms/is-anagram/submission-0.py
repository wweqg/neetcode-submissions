class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm1 = {}
        hm2 = {}

        for c in s:
            hm1[c] = hm1.get(c, 0) + 1
        
        for c in t:
            hm2[c] = hm2.get(c, 0) + 1
        
        return hm1 == hm2