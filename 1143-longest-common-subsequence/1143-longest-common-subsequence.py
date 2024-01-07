class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D- dp probles
        # create a matrix grid and store the LCS ( longest common subsequence) 
        # when char matches then we just remove them and see only remaining string as subproblems (diagonally bottom right cell)
        # when char does not match we have 2 possible sub problems - 1 - remove char1 from text1 and keep char2 in text2 to find LCS (bottom cell)
        # -2 - keep char1 from text1 and remove char2 in text2 to find LCS (right cell)
        # return max that is present at 0,0 position in the grid 
        
        rows,cols = len(text1) , len(text2) 
        grid = [[ 0 for i in range(cols)] for j in range(rows)]
        
        for r in range(rows-1,-1,-1):
            for c in range(cols-1,-1,-1):
                
                if text1[r] == text2[c]:
                    # check digonally bottom right 
                    grid[r][c] = (grid[r+1][c+1] if (r+1< rows and c+1 < cols) else 0 ) + 1
                else:
                    # check max of bottom and right 
                    grid[r][c] = max ((grid[r+1][c] if (r+1< rows) else 0 ), (grid[r][c+1] if (c+1 < cols) else 0 ))
                    
        return grid[0][0]
                