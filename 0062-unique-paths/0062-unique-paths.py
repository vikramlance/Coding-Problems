class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        r,c = m,n
        
        # finsh = r-1 , c-1
        grid_cache = [ [0 for i in range(c)] for j in range(r)]
        
        grid_cache[r-1][c-1] = 1
        
        for row in range(r-1,-1,-1):
            
            for col in range(c-1,-1,-1):
                # print(row, col, grid_cache[row][col])
                grid_cache[row][col] +=  (grid_cache[row+1][col] if row + 1 < r else 0) + (grid_cache[row][col+1] if col + 1 < c else 0)
                    
                # print('row, col', grid_cache[row][col])
                
        return grid_cache[0][0]