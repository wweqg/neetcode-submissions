class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in hm:
                hm[ss] = []
            hm[ss].append(s)        
        res = []

        for _, value in hm.items():
            res.append(value)
        
        return res