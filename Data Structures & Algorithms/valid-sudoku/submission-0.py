class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set)

        n = len(board)
        m = len(board[0])

        for i in range(n):
            for j in range(m):
                curr = board[i][j]

                if curr == ".":
                    continue

                if curr in row[i] or curr in col[j] or curr in grid[(i//3, j//3)]:
                    return False

                row[i].add(curr)
                col[j].add(curr)
                grid[(i//3, j//3)].add(curr)
        
        return True