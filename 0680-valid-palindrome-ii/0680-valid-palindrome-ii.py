class Solution:
    def validPalindrome(self, s: str) -> bool:
        # ebcbbececab bacecbbcbe
        
        def is_palin(s):
            l,r = 0, len(s) -1
            while l< r:
                if s[l] != s[r]:
                    return False
                else:
                    r -= 1
                    l += 1
            return True
            
        l,r = 0, len(s) -1
        deleted_char = 0
        while l< r:
            if s[l] != s[r]:
                if deleted_char>0:
                    return False
                else:
                    deleted_char += 1
                    return is_palin(s[l:r]) or is_palin(s[l+1:r+1])
            else:
                r -= 1
                l += 1
        return True
        
        
        
                
        
        