class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # counting sort
        count = [0]*(len(nums)+1)
        repeated = 0
        missing = 0
        for i in nums:
            count[i] += 1
            if count[i] > 1:
                repeated = i
        for index, c in enumerate(count):
            if index > 0 and c == 0:
                missing = index
        
        return [repeated, missing]
                