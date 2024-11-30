class Solution:
    def maximumCount(self, nums: List[int]) -> int:
#         brute - count all neg, pos and max(pos , neg)
#         binary - find pivot index , exclude zeros 
        

        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
        
        l, r = 0, len(nums) - 1
        idx_neg = None
        
        while l<=r:
            # idx_neg 
            mid = l + (r-l)//2
            if nums[mid] < 0: # and nums[mid + 1] >=0:
                idx_neg = mid
                l = mid + 1
            # elif nums[mid] < 0 and nums[mid + 1] < 0:
                # l = mid + 1
            else:
                r = mid -1
                
        # nums = [-1,0,2,3,4]
        # l = 1 r= 0
        # idx = 1
        
        l, r = 0, len(nums) - 1
        idx_pos = None
        while l<=r:            
            mid = l + (r-l)//2
            if nums[mid] > 0 : #and nums[mid - 1] <= 0
                idx_pos = mid
                r = mid -1 
                # break
            # elif nums[mid] > 0 and nums[mid - 1] > 0:
                # r = mid - 1
            else:
                l = mid + 1
        
        if idx_neg is None:
            neg = 0
            
        else:
            neg = idx_neg + 1
            
        
        if idx_pos is None:
            pos = 0
        else:
            pos = len(nums) - idx_pos
            
            
        return max(pos,neg)
        