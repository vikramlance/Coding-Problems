class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # hello ll
        n = len(needle) # 2
        h = len(haystack)  # 5
        for i in range(h - n + 1):
            # i - 0 1 2 3
            if haystack[i:i+n]== needle:
                return i
        return -1
            