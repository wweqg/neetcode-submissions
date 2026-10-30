class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = []
        res = []

        def dfs(l, r):
            if l == r == n:
                res.append(''.join(s))
                return
            if l < n:
                s.append('(')
                dfs(l+1, r)
                s.pop()
            
            if r < l:
                s.append(')')
                dfs(l, r+1)
                s.pop()
            
            return
        
        dfs(0, 0)

        return res