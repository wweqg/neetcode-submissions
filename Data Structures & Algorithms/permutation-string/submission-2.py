class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        c1 = [0] * 26
        c2 = [0] * 26

        for c in s1:
            c1[ord(c) - ord('a')] += 1

        if len(s2) < n:
            return False

        l = 0
        r = l + n - 1

        for i in range(n):
            c2[ord(s2[i]) - ord('a')] += 1
        
        if c1 == c2:
            return True

        while r < len(s2) - 1:
            c2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            c2[ord(s2[r]) - ord('a')] += 1

            if c1 == c2:
                return True
        
        return False

