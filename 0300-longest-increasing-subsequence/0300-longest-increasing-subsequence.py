class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] is lis for list until ith element 
        # for i = 0 - base case - dp[0] = 1 
        # i = 2 if nums[i] < nums[j]
        
        
        # use j for iterating dp , use i for iterating nums 
        
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
        
        
        