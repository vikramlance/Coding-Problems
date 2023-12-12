class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # brute force - check every element product, assing it to max and then find max(max_prev, max_cur)
        max_product = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = (nums[i] - 1) * (nums[j] - 1)
                max_product = max(prod, max_product)
        return max_product
        