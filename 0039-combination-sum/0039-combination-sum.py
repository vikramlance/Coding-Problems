class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res= []
        
        cur_set = []
        
        def dfs(i, total):
            if target < total or i >= len(candidates):
                return 
            if target == total:
                res.append(cur_set.copy())
                return 
            
            total += candidates[i] 
            cur_set.append(candidates[i])
            dfs(i, total)
            
            cur_set.pop()
            total -= candidates[i] 
            dfs(i+1, total)
        
        dfs(0, 0)
        return res