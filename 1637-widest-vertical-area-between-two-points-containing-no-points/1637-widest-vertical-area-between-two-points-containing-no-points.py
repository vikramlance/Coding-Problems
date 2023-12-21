class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        x_cordinates = []
        for i in points:
            x_cordinates.append(i[0])
        
        sorted_x_cordinates = sorted(x_cordinates)
        
        max_diff = 0
        
        for i in range(1,len(sorted_x_cordinates)):
            
            if max_diff < sorted_x_cordinates[i] - sorted_x_cordinates[i-1]:
                max_diff = sorted_x_cordinates[i] - sorted_x_cordinates[i-1]
                
        return max_diff
        
        