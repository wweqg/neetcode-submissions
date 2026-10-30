class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = [0] * 26
        arr2 = [0] * 26

        for c in s:
            arr1[(ord(c) - ord('a'))] += 1

        for c in t:
            arr2[(ord(c) - ord('a'))] += 1

        return arr1 == arr2