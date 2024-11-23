class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:  # Base case: empty list
            return -1
        
        mid = len(nums) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            result = self.search(nums[:mid], target)  # Search left half
            return result if result != -1 else -1  # Adjust index if found
        else:
            result = self.search(nums[mid + 1:], target)  # Search right half
            return mid + 1 + result if result != -1 else -1  # Adjust index
