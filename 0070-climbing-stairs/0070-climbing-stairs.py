class Solution:
    def climbStairs(self, n: int) -> int:
        # 
        # dp[i] = dp[i-1] + dp[i-2]
        # for 3 , steps to reach 2 + steps to reach 1 , 2 + 1 = 3 
        dp = [0,1]
        # dp[0] = 0
        # dp[1] = 1
        
        # 0 1 2
        # 1,1 1,2 2,3
        for i in range(n):
            temp = dp[1]
            
            dp[1] = dp[1] + dp[0]
            dp[0] = temp
            
        return dp[1]