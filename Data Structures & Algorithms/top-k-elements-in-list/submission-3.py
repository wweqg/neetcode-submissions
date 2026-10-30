class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort
        count = dict()

        for n in nums:
            count[n] = count.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for key, count in count.items():
            bucket[count].append(key)

        ret = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                ret.append(n)
                if len(ret) == k:
                    return ret
        
        return ret
