class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l,r = 0, len(s) -1 
        # 0 , 3 
        while l<r:
            s[l] , s[r] = s[r] , s[l]
            l += 1
            r -= 1
            
#         def rev(s):
#             if len(s) <= 1:
#                 return s
            
#             else:
#                 print(s)
#                 return [s[-1]] + rev(s[:len(s)-1])
        
#         s = rev(s)
#         print('xxxxx', s)
        # s = [a b c] -- len 3  ret [c rev(a b)] ret [b rev(a)]