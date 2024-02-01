class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) % 3 != 0:
            return []
        nums = sorted(nums)
        res = []
    
        for i in range(0,len(nums)-2,3):
            if nums[i+2] - nums[i] <= k:
                res.append(nums[i:i+3])
            else:
                return []
        return res