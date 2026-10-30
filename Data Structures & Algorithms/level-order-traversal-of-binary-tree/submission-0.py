# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        q.append(root)
        res = []

        if not root:
            return res

        while q:
            ne = []
            tmp = []
            for node in q:
                tmp.append(node.val)
                if node.left:
                    ne.append(node.left)
                if node.right:
                    ne.append(node.right)
            res.append(tmp)
            q = ne
        
        return res