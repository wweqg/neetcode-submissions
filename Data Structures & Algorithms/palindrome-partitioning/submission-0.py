class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, j, arr):
            if j >= len(s):
                if i == j:
                    res.append(arr.copy())
                return
            
            if self.isPali(s, i, j):
                arr.append(s[i:j+1])
                dfs(j+1, j+1, arr)
                arr.pop()
            
            dfs(i, j+1, arr)
        
        dfs(0, 0, [])
        return res
        
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True