class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        max_freq = 0
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] > max_freq:
                max_freq = counter[i]
        total_freq = 0
        for j in counter:
            if counter[j] == max_freq:
                total_freq += max_freq
        return total_freq
        
        