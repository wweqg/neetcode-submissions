class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        hm = dict()
        most = 0

        while r < len(s):
            curr = s[r]
            hm[curr] = hm.get(curr, 0) + 1
            most = max(most, hm[curr])

            while (r-l+1 - most) > k:
                hm[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

            r += 1
        
        return res