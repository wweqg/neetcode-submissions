class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm = {}
        for c in t:
            hm[c] = 1 + hm.get(c, 0)
        res = ''
        resLen = float('inf')
        window = {}
        l = 0
        have = 0
        needed = len(hm)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in hm and hm[c] == window[c]:
                have += 1
            
            while have == needed:
                if (r-l+1) < resLen:
                    res = s[l:r+1]
                    resLen = (r-l+1)
                lc = s[l]
                window[lc] -= 1
                if lc in hm and window[lc] < hm[lc]:
                    have -= 1
                l += 1

        return res if resLen != float('inf') else ""

