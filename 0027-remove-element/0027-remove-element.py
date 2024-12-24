class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l, r = 0, 0
        # l = 4 r =5  [0 1 3 3 4 2 2]
        for r in range(len(nums)):            
            if nums[l] == val and nums[r] != val:
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
            
            if nums[l] != val:
                l += 1
        return l
        # for j in range(len(nums)):
        #     if nums[j] == val:
        #         return j
        
                