class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l = 0
        r = 0
        res = []
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
            if l > q[0]:
                q.popleft()
        
        return res
