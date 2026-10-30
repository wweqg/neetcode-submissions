class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        res = 0
        for idx, h in enumerate(heights):
            if not st:
                st.append((idx, h))
            elif h < st[-1][-1]:
                tmp = idx
                while st and h < st[-1][-1]:
                    i, ih = st.pop()
                    area = ih * (idx - i)
                    res = max(res, area)
                    tmp = i
                st.append((tmp, h))
            else:
                st.append((idx, h))
        
        for idx, h in st:
            area = h * (n - idx)
            res = max(area, res)
        
        return res

