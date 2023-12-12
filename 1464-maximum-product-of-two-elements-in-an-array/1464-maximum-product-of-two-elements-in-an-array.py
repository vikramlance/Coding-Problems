class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force - check every element product, assign it to max and then find max(max_prev, max_cur)
        # max_product = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         prod = (nums[i] - 1) * (nums[j] - 1)
        #         max_product = max(prod, max_product)
        # return max_product
        
        
        # optimization - find max and second max those will produce max product as all elements are positive
        max1 = max(nums)
        nums.remove(max1)
        
        max2 = max(nums)
        
        return (max1-1)*(max2-1)