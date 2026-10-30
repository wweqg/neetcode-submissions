class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = [0] * 26
        for c in s1:
            count[ord(c) - ord('a')] += 1
        
        k = len(s1)
        window = [0] * 26
        
        # Early return if s2 is smaller than s1
        if len(s2) < k:
            return False
        
        # Initialize the window with the first k characters of s2
        for i in range(k):
            window[ord(s2[i]) - ord('a')] += 1
        
        # Check if the initial window matches the count of s1
        if window == count:
            return True
        
        # Slide the window over s2
        for l in range(1, len(s2) - k + 1):
            window[ord(s2[l - 1]) - ord('a')] -= 1
            window[ord(s2[l + k - 1]) - ord('a')] += 1
            
            # Check if the current window matches the count of s1
            if window == count:
                return True
        
        return False
