class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, s):
            if s == target:
                res.append(curr.copy())
                return
            
            if i >= len(nums) or s > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, s+nums[i])
            curr.pop()
            dfs(i+1, curr, s)

        dfs(0, [], 0)

        return res

            
