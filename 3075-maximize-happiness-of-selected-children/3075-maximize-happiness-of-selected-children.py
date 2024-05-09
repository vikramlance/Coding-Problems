class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        happiness = sorted(happiness, reverse=True)
        res = 0 
        
        for i in range(k):
            remaining = happiness[i] - i
            if remaining > 0:
                res += remaining
        return res
        