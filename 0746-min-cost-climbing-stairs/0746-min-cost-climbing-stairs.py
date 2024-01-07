class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # dp[i] = cost[i] + min(dp[i-1],dp[i-2])
        
        dp = [0,0]
        # from example1 from 15 climb 2 steps, means the last step is out of the cost array so add 0 to cost array
        cost.append(0)
        for price in cost:
            temp = dp[1]
            dp[1] = price + min(dp[0], dp[1])
            dp[0] = temp
        return dp[1]
            
        