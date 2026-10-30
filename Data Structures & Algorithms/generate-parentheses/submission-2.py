class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(arr, l, r, curr):
            if l == n and r == n:
                arr.append(curr)
                return
            if l < n:
                dfs(arr, l + 1, r, curr + "(")
            if r < l:
                dfs(arr, l, r + 1, curr + ")")
        
        a = []
        dfs(a, 0, 0, "")
        return a