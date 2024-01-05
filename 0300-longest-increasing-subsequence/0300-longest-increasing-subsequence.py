class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] is lis for list until ith element for example nums = [4,56,100] then dp = [1,2,3]
        # set all the dp elements to 1 cause minimum lis is 1 ( that is the elements itself if no other element is dound that is greater than the current element)
        # iterate over nums and for each sub array dp 0 to i -1 , we check if nums[i] > nums[j] if it is greater then we update the dp to max dp[i], dp[j] + 1 
        
        
        dp = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
        
        
        