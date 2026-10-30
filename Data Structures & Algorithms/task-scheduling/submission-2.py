class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}
        for t in tasks:
            hm[t] = 1 + hm.get(t, 0)
        
        arr = []

        for v in hm.values():
            arr.append(-v)
        
        heapq.heapify(arr)
        cooldown = []
        time = 0

        while arr or cooldown:
            if arr:
                curr = heapq.heappop(arr)
                curr = -curr
                curr -= 1
                if curr != 0:
                    cooldown.append((curr, time + n))

            if cooldown:
                if time == cooldown[0][1]:
                    tmp = cooldown.pop(0)
                    heapq.heappush(arr, -tmp[0])
            
            time += 1
        
        return time