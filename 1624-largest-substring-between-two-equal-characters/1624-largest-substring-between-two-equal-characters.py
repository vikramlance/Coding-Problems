class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        longest = -1
        for i in range(len(s)):
            char = s[i]
            if char in char_index:
                len_substring = i - char_index[char] - 1 
                if len_substring > longest:
                    longest = len_substring
            else:
                char_index[char] = i
        return longest
            
        