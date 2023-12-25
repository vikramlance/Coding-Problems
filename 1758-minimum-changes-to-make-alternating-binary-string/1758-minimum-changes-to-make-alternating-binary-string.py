class Solution:
    def minOperations(self, s: str) -> int:
        # 01110 1000 00000 001 0 - 0 1 - 1 2 - 0 
        
        count = 0
        for i in range(len(s)):
            if i % 2 != int(s[i]):
                count += 1
        
        return min(count, len(s) - count)
                    
       