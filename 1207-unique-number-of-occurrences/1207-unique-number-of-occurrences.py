class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # value of i is from -1000 to 1000 so we can use counting sort
        # first frequency of the nums and then count the frequency 
        
        nums = [0]*2001
        count = [0]*1001
        
        for i in arr:
            nums[i+1000] += 1
        
        for k in range(2001):
            if nums[k] and count[nums[k]] + 1 > 1:
                return False
            count[nums[k]] += 1
        
        return True
        
        """
        1001 1 
        1002 1
        
        0-1000
        """