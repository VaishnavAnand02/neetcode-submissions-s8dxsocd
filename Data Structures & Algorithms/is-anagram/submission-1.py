class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arrcount= [0]*26
        for ch in s:
            arrcount[ord(ch)-ord('a')] += 1
        for ch in t:
            arrcount[ord(ch)-ord('a')] -= 1
        for ct in arrcount:
            if ct > 0:
                return False
        
        return True