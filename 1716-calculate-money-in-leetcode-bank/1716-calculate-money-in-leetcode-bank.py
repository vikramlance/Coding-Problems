class Solution:
    def totalMoney(self, n: int) -> int:
               
        last_monday_contri = 0
        total = 0 
        
        for i in range(n):
            if i % 7 == 0:
                total += last_monday_contri + 1
                last_monday_contri += 1
                prev = last_monday_contri
            else:
                total += prev + 1
                prev += 1
        return total
                