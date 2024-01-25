# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        
        freq = defaultdict(int)
        odds = 0 
        
        
        def dfs(root):
            nonlocal odds
            
            if not root:
                return 0
            
            freq[root.val] += 1  
            change = 1 if freq[root.val] % 2 == 1 else -1
            odds += change
            
            if not root.left and not root.right:
                res = 1 if odds <= 1 else 0
            else:
                res = dfs(root.left) + dfs(root.right)
            
            odds -= change
            freq[root.val] -= 1
            
            return res
        
        return dfs(root)
            
            
            
        