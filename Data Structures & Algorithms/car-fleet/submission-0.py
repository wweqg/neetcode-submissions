class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(pos, speed) for pos, speed in zip(position, speed)]
        st = []
        pair.sort(reverse=True)

        for p, s in pair:
            t = (target - p) / s

            if not st or t > st[-1]:
                st.append(t)
        
        return len(st)