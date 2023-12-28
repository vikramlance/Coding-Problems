class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # abaac 12345 
        # aabaa 
        total = 0 
        
        l, r = 0, 0
        length = len(colors)
        while l <= r and r < length:
            
            if colors[l] != colors[r]:
                time = sum(neededTime[l:r]) - max(neededTime[l:r])
                total += time
                l = r
                # r += 1
            # elif colors[l] == colors[r] :
            #     r += 1
            elif colors[l] == colors[r] and r == length - 1:
                time = sum(neededTime[l:r+1]) - max(neededTime[l:r+1])
                total += time
                # r += 1
            r += 1
                
        return total 
        