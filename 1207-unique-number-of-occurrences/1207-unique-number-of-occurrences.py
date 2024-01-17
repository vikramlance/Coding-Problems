class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # value of i is from -1000 to 1000 so we can use co
        
        freq = {}
        
        for i in arr:
            freq[i] = freq.get(i, 0) + 1
        
        count_set = set()
        
        for count in freq.values():
            if count not in count_set:
                count_set.add(count)
            else:
                return False
        return True
        