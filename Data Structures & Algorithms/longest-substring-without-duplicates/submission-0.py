class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            curr = s[r]
            while curr in hs:
                tmp = s[l]
                hs.remove(tmp)
                l += 1
            hs.add(curr)
            res = max(res, r-l+1)
            r += 1
        return res
        