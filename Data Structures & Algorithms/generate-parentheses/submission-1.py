class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        def dfs(l, r):
            if l == r and r == n:
                res.append("".join(s.copy()))
                return
            if l < n:
                s.append('(')
                dfs(l+1, r)
                s.pop()
            
            if r < l:
                s.append(')')
                dfs(l, r+1)
                s.pop()
        dfs(0, 0)
        return res