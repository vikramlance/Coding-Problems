class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        from collections import deque
        p_que = deque()
        n_que = deque()
        
        for i in nums:
            if i > 0:
                p_que.append(i)
            else:
                n_que.append(i)
                
        
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] =  p_que.popleft()
            else:
                nums[i] =  n_que.popleft()
        
        return nums