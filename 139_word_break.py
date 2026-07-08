class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # check dp[i], if dp[j] is true (previous word) and can substring [j:i] become word?
        
        # word_set = set(wordDict)
        # n = len(s)
        # dp = [False] * (n+1)
        # dp[0] = True # empty string (base case)
        # max_length = max(map(len, wordDict)) # find max length of word

        # for i in range(1, n+1):
        #     for j in range(max(0, i - max_length), i): # iterate j from max length of word
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break
        
        # return dp[n]

        # top down
        dp = [False] * (len(s) + 1) # 0 to 8
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1): # start from 7, until 0
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

        # time: O(n * m * L) n = len(s), m = len(wordDict), L = max word length
        # space: O(n)