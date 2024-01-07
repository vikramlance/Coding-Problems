class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows,cols = len(obstacleGrid), len(obstacleGrid[0])
        grid_cache = [[0 for i in range(cols)] for j in range(rows)]
        # Edge case - when obstacle is present at bottom-right corner the return 0
        if obstacleGrid[rows-1][cols-1] == 0:
            grid_cache[rows-1][cols-1] = 1
        else:
            return 0
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                grid_cache[r][c] += (grid_cache[r+1][c] if (r+1< rows and obstacleGrid[r][c] == 0) else 0)  + (grid_cache[r][c+1] if (c+1< cols and obstacleGrid[r][c] == 0) else 0)
        return grid_cache[0][0] 