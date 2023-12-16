class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sd = {}
        
        for path in paths:
            sd[path[0]] = path[1]
        
        for source,dest in sd.items():
            
            if dest not in sd.keys():
                return dest