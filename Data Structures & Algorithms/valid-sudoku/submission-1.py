class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                val = board[i][j]
                if val in row[i] or val in col[j] or val in grid[(i//3, j//3)]:
                    return False
        
                row[i].add(val)
                col[j].add(val)
                grid[(i//3, j//3)].add(val)
        
        return True
                