class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        
        res= 0
        res_zero = None
        for i in range(2, len(num)):
            if num[i] == num[i-1] == num[i-2]:
                if num[i] == "0":
                    res_zero = "000"
                res = max(res, int(num[i-2:i+1]))
        
        if res == 0:
            if res_zero:
                return res_zero
            else:
                return ""
        else:
            return str(res)