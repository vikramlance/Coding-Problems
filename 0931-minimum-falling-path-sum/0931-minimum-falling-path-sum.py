class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 6 - 13 , 5 - 12, 4 - 12 
        # 2 - 14, 1- 13, 3 - 15 
        rows = cols = len(matrix) 
        # cache to store minimum sum at given cell 
        grid = [[0 for c in range(cols)] for r in range(rows)]
        # copy last row of matrix as that is minimum sum for each cell
        grid[-1] = matrix[-1]
        
        for r in range(rows-2,-1,-1):
            for c in range(cols-1,-1,-1):
                
                below = grid[r+1][c] if 0 <= r+1 < rows and 0 <= c < cols else float('inf') 
                below_right = grid[r+1][c+1] if 0 <= r+1 < rows and 0 <= c+1 < cols else float('inf')
                below_left = grid[r+1][c-1] if 0 <= r+1 < rows and 0 <= c-1 < cols else float('inf')
                
                grid[r][c] = matrix[r][c] + min(below, below_right, below_left)
                
        return min(grid[0])