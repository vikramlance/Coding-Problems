class Solution:
    def maxScore(self, s: str) -> int:
        
        count_ones = 0
        for i in s:
            if i == "1":
                count_ones += 1
        max_score = cur_score = count_ones
        for i in range(len(s)):
            if s[i] == "0":
                cur_score += 1
                if i == len(s) - 1:
                    cur_score -= 1
            else:
                cur_score -= 1
                if i == 0:
                    max_score -=1
            
            max_score = max(max_score, cur_score)
        
        return max_score