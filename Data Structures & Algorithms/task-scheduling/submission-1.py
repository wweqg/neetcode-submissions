class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hm = {}

        for t in tasks:
            if not hm.get(t):
                hm[t] = 0
            hm[t] += 1
        
        arr = []

        for _, val in hm.items():
            arr.append(-val)
        
        heapq.heapify(arr)

        cool = []

        time = 0

        while arr or cool:
            if arr:
                ele = heapq.heappop(arr)
                ele += 1
                if ele < 0:
                    cool.append((ele, time+n))
            
            if cool:
                if time == cool[0][1]:
                    ele, _ = cool.pop(0)
                    heapq.heappush(arr, ele)

            time += 1
        
        return time


