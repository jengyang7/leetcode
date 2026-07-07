class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # find the len of the needle
        # loop thru the char of haystack, if found first char match, check the string match

        n = len(needle)

        for i in range(len(haystack) - n + 1):
            if haystack[i:i+n] == needle:
                return i
        
        return -1

        # time: O(n)
        # space: O(1)