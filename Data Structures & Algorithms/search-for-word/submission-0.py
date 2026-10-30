class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = set()
        def dfs(x, y, i):
            if i == len(word):
                return True
            if x < 0 or y < 0 or x >= n or y >= m:
                return False
            if (x, y) in visited:
                return False
            if word[i] == board[x][y]:
                visited.add((x,y))
                found = dfs(x, y+1, i+1) or dfs(x, y-1, i+1) or dfs(x+1, y, i+1) or dfs(x-1, y, i+1)
                visited.remove((x,y))
                return found
            return False
        
        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j]:
                    if dfs(i, j, 0):
                        return True
        return False
            
