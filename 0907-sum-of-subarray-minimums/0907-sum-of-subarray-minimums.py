class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        # brute force
        total = 0
        for i in range(len(arr) ):
            
            for j in range(len(arr)-i+1):
                sub = arr[j:j + i]
                # print(sub)
                total += min(sub if sub else [0])
        total += min(arr)
        return total % ((10**9) + 7)
        """
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result 
