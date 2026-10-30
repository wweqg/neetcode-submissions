class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = [0] * numCourses
        hm = {}

        for course, prereq in prerequisites:
            req[course] += 1
            if not prereq in hm:
                hm[prereq] = []
            hm[prereq].append(course)
        
        q = deque()
        for idx, prereq in enumerate(req):
            if prereq == 0:
                q.append(idx)
        
        while q:
            curr = q.popleft()
            if curr in hm: 
                for c in hm[curr]:
                    req[c] -= 1
                    if req[c] == 0:
                        q.append(c)
        
        for r in req:
            if r > 0:
                return False

        
        return True