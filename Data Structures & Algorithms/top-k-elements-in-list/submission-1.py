from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency hashmap
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1

        # Bucket sort based on frequency
        freq = [[] for _ in range(len(nums) + 1)]  # A list of lists
        for num, count in hm.items():
            freq[count].append(num)  # Append the number to the correct frequency bucket

        # Collect the top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Iterate from high frequency to low
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
