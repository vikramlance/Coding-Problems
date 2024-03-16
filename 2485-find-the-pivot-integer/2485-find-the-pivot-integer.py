class Solution:
    def pivotInteger(self, n: int) -> int:
        
        cur_sum = 0 
        total = n*(n + 1) / 2
        
        for i in range(1, n + 1):
            cur_sum = i*(i + 1) / 2
            if cur_sum == total - cur_sum + i:
                return i
        return -1
        
#         if n == 1:
#             return 1
        
#         right_sum = total = (n * (n + 1)) / 2
#         left_sum = 0
#         mid = n
#         while right_sum >= left_sum:
#             mid = (mid + 1)/2

#             left_sum =  (mid (mid + 1)) / 2 
#             right_sum = total - left_sum

#             if left_sum == right_sum:
#                 return mid
#         return -1
            
        