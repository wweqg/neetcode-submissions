"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        hm = {}
        q = deque()
        ne = Node(node.val)
        hm[node] = ne
        q.append(node)

        while q:
            curr = q.popleft()

            for nei in curr.neighbors:
                if not nei in hm:
                    hm[nei] = Node(nei.val)
                    q.append(nei)
                hm[curr].neighbors.append(hm[nei])
        
        return hm[node]

