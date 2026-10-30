class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""

        for s in strs:
            l = len(s)
            ret += str(l) + "#" + s
        
        return ret


    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            ret.append(s[j+1:j+1+l])
            i = j + l + 1
        return ret






