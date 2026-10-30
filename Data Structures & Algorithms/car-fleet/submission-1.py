class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = [(pos, sp) for pos, sp in zip(position, speed)]
        arr = sorted(arr, reverse=True)
        s = []

        for pos, sp in arr:
            t = (target - pos)/sp
            if not s:
                s.append(t)
                continue
            if t > s[-1]:
                s.append(t)

        return len(s)