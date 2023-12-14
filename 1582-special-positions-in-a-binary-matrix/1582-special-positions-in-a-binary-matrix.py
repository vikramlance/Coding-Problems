class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # brute 
        rows, cols = len(mat), len(mat[0])
        count = 0
        for r in range(rows):
            if sum(mat[r]) == 1: 
                for c in range(cols):
                    if mat[r][c] == 1:
                        total = 0
                        for i in range(rows):
                            total += mat[i][c]
                        if total == 1:
                            count += 1
        return count 
                            
                
                
                
                            
                