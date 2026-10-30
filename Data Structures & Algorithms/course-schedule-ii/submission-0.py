class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [0] * numCourses
        hm = {}

        for c, pre in prerequisites:
            if not pre in hm:
                hm[pre] = []
            hm[pre].append(c)
            req[c] += 1
        
        q = deque()
        res = []

        for idx, r in enumerate(req):
            if r == 0:
                q.append(idx)

        while q:
            curr = q.popleft()
            res.append(curr)
            if curr in hm:
                for c in hm[curr]:
                    req[c] -= 1
                    if req[c] == 0:
                        q.append(c)
        
        for r in req:
            if r > 0:
                return []
        
        return res