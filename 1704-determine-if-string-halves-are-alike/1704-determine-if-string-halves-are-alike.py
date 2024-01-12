class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)
        a = s[:length//2]
        b = s[length//2:]
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}        
        
        def helper(string):
            count = 0
            for i in string:
                if i in vowels:
                    count +=1
            return count
        
        return helper(a) == helper(b)