class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_subset = []
        def dfs(i):
            # base case
            if i >= len(nums):
                res.append(curr_subset.copy())
                return 
            
            # include i
            curr_subset.append(nums[i])
            dfs(i+1)
            
            
            # exclude i
            curr_subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res
            
            
            