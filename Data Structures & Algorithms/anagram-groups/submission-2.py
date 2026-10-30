class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {} # [str]: [str]

        for s in strs:
            tmp = [0] * 26
            for c in s:
                tmp[ord(c) - ord("a")] += 1
            arr = hm.get(tuple(tmp), [])
            arr.append(s)
            hm[tuple(tmp)] = arr
        
        ret = []

        for arr in hm.values():
            ret.append(arr)
        
        return ret