class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while monoStack and temperatures[monoStack[-1]] < t:
                idx = monoStack.pop()
                res[idx] = i - idx
            monoStack.append(i)
        
        return res