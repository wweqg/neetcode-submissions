class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoDe = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while monoDe and temperatures[monoDe[-1]] < t:
                idx = monoDe.pop()
                res[idx] = i - idx
            monoDe.append(i)
        return res