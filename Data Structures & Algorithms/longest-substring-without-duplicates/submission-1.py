class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()

        l = 0
        r = 0
        count = 0

        while r < len(s):
            curr = s[r]

            while curr in hs:
                hs.remove(s[l])
                l += 1
                
            hs.add(curr)
            count = max(count, len(hs))

            r += 1

        return count
