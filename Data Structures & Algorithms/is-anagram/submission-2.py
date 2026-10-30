class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 52

        for c in s:
            arr[(ord(c) - ord('a'))] += 1

        for c in t:
            arr[(ord(c) - ord('a'))+26] += 1

        return arr[:26] == arr[26:]