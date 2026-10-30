class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ret = [0] * len(temperatures)

        for idx, t in enumerate(temperatures):
            if not s:
                s.append(idx)
                continue
            
            while s and temperatures[s[-1]] < t:
                i = s.pop()
                ret[i] = idx-i
            
            s.append(idx)
        
        return ret