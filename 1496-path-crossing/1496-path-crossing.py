class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        
        directions = {"N": (0,1), "E": (1,0), "S": (0,-1), "W": (-1,0) }
        
        cur = prev = (0, 0)
        seen.add(cur)
        # 00 01 11 10 00
        for p in path:
            
            cur = (prev[0] + directions[p][0], prev[1] + directions[p][1])
            # print(cur)
            if cur in seen:
                return True 
            seen.add(cur)
            prev = cur
            # print(seen, 'aaaaaaa')
        return False
            
            
            