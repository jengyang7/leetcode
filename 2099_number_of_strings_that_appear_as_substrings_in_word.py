class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # iterate patterns, check if the str is substring of word

        res = 0

        for n in patterns:
            if n in word:
                res += 1

        return res

        # time: O(n)
        # timeL O(1)