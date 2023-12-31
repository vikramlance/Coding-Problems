class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_index = {}
        longest = -1
        for i in range(len(s)):
            char = s[i]
            if char in char_index:
                char_index[char][1] = i
            else:
                char_index[char] = [i,i]
            longest = max(longest, char_index[char][1] - char_index[char][0] -1)
        return longest
            
        