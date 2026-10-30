class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            '(':')',
            '{':'}',
            '[':']'
        }

        st = []
        
        for c in s:
            if c in hm:
                st.append(c)
            else:
                if not st:
                    return False
                tmp = st.pop()
                if c != hm[tmp]:
                    return False
        return len(st) == 0