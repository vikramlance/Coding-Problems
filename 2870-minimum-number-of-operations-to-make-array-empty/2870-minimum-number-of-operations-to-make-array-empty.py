class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # 0 index array positive int equal - delete 2 or 3 
        # min num of ops or -1 
        
        # apply 3 equal then 2 equal so get count of each element 
        # if count == 1 then -1 , count % 3 == 0 then add division else division + 1 to result
        
        res = 0 
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        if 1 in freq.values():
            return -1
        
        for k, count in freq.items():
            div = count // 3
            if count % 3 == 0:
                res += div
            else:
                res += div + 1
        return res
            
        