class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        
        for i in s:
            d_s[i] = d_s.get(i,0)+1
        for i in t:
            d_t[i] = d_t.get(i,0)+1
        
        return d_s == d_t

        