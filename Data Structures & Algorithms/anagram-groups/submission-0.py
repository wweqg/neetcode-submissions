class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in hm:
                hm[tmp] = []
            hm[tmp].append(s)
        
        res = []

        for _, v in hm.items():
            res.append(v)
        
        return res