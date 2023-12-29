class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        # time comp O(n*n*n) bab
         
        if len(s) ==1:
            return s
        
        max_palin_str = '' 
        for i in range(len(s)-1):
            for j in range(i, len(s)):
                if self.palindrome(s[i:j+1]) and len(s[i:j+1]) > len(max_palin_str):
                    max_palin_str = s[i:j+1]
                    
            
        return max_palin_str
    
    def palindrome(self, s):

        l,r = 0, len(s) -1
        while l<r:
            if s[l] != s[r]:
                return False
            else:
                l,r = l+1, r-1
        return True
            
        """
        
        max_len = 0
        max_str = ""
        max_str_l, max_str_r = 0,0
        for i in range(len(s)):
            #odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l] ==s[r]:
                if r - l + 1 > max_len:
                    max_len =  r - l + 1 
                    max_str_l = l
                    max_str_r = r
                l -= 1
                r += 1
            # even length 
            #odd length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l] ==s[r]:
                if r - l + 1 > max_len:
                    max_len =  r - l + 1 
                    max_str_l = l
                    max_str_r = r
                l -= 1
                r += 1
                
        return s[max_str_l:max_str_r+1]