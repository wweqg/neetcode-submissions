class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        resLen = float('inf')
        l = 0
        r = 0
        count = dict()

        for c in t:
            count[c] = count.get(c, 0) + 1
        
        have = 0
        needed = len(count)
        window = dict()

        while r < len(s):
            curr = s[r]
            window[curr] = window.get(curr, 0) + 1

            if curr in count and window[curr] == count[curr]:
                have += 1
            
            while have == needed:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    res = s[l:r+1]
                head = s[l]
                window[head] -= 1
                l += 1
                if head in count and window[head] < count[head]:
                    have -= 1

            r += 1


        return res    

        