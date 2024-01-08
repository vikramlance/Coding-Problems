class Solution:
    def rob(self, nums: List[int]) -> int:
        # we can consider 2 cases - include 1st house and exclude last house or vice versa
        if len(nums) ==1:
            return nums[0]
        prev_house, prev_to_prev_house = 0,0
        
        # exclude first house
        for i in range(1, len(nums)):
            temp = prev_house
            prev_house = max(prev_house, prev_to_prev_house + nums[i])
            prev_to_prev_house = temp
        
        max1 = prev_house
        # print(max1)
        
        prev_house, prev_to_prev_house = 0,0
        # include first house
        for i in range(len(nums)-1):
            temp = prev_house
            prev_house = max(prev_house, prev_to_prev_house + nums[i])
            prev_to_prev_house = temp
        
        max2 = prev_house
        # print(max2)
        
        return max(max1,max2)