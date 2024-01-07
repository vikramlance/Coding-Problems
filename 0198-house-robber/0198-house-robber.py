class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, ..]
        # dp[i] = max(dp[i-2] + i, dp[i-2])
        dp = [0,0]
        
        for i in range(len(nums)):
            temp = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = temp
        return dp[1]
        