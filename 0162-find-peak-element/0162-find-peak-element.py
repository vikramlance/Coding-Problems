class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
         # [1,2,1,3,5,6,4] [1,2,3,1]
        # edge cases
        if len(nums) == 1 or nums[0]>nums[1]:
            return 0
        if nums[len(nums) -1]>nums[len(nums) -2]:
            return len(nums) -1
        
        l,r = 0,len(nums) -1
        
        while l<= r:
            mid = (l+r) // 2
        
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid +1]:
                return mid
            # move in the direction of incresing value cause if nums[-1] is not peak element which we already checked in edge cases
            # we are garuneeted to get peok element 
            elif nums[mid] > nums[mid-1] :
                l = mid
            elif nums[mid] > nums[mid+1] :
                r = mid
            else:
                r = mid
  