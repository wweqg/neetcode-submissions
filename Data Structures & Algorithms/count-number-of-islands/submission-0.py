class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        marked = set()
        res = 0

        n = len(grid)
        m = len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= n or y >= m or (x,y) in marked:
                return
            if grid[x][y] == "0":
                return
            
            marked.add((x,y))
            dfs(x, y+1)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x-1, y)

        for i in range(n):
            for j in range(m):
                if not (i, j) in marked and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        
        return res
