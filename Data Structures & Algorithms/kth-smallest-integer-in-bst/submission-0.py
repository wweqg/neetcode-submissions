# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = [k, 0]

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            arr[0] = arr[0] - 1
            if arr[0] == 0:
                arr[1] = node.val
                return 
            dfs(node.right)
            return
        
        dfs(root)
        return arr[1]