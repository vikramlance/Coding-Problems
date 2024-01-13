class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        freq_s = {}
        for i in s:
            freq_s[i] = freq_s.get(i,0) + 1
            
        freq_t = {}
        for i in t:
            freq_t[i] = freq_t.get(i,0) + 1
        
        
        res = 0
        for i in freq_t:
            if freq_t[i] > freq_s.get(i,0):
                res += freq_t[i] - freq_s.get(i,0) 
                
        return res
