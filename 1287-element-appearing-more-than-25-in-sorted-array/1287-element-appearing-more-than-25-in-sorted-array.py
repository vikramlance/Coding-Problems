class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # sorted - 25% 
        min_count = len(arr) / 4
        
        cur_count = 1      
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                cur_count +=1
            else:
                if cur_count > min_count:
                    return arr[i-1]
                cur_count = 1
        if cur_count > min_count:
            return arr[-1]
        
        