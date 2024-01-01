class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # sort g and s , g[i] <= s[j] increment count, i , j else increment j  7 8 9 10,  5 6 7 8 
        
        g, s = sorted(g), sorted(s)
        i,j = 0,0
        count = 0
        
        while i < len(g) and j<len(s):
            if g[i] <= s[j]:
                count +=1
                i +=1
                j +=1
            else:
                j +=1
        return count