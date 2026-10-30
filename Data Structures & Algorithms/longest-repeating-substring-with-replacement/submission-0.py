class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        hm = {}
        l = 0
        maxf = 0
        for r in range(n):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxf = max(maxf, hm[s[r]])
            if (r-l+1 - maxf) > k:
                hm[s[l]] -= 1
                l += 1
        
        return r-l+1