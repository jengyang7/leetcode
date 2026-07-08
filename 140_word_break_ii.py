class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]
            
            if start in memo:
                return memo[start]
            
            results = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        if sub == "":
                            results.append(word)
                        else:
                            results.append(word + " " + sub)
            
            memo[start] = results
            return results
        
        return dfs(0)

        # Time: O(2^n * n), because there can be exponentially many valid sentences, and building each sentence can take O(n).

        # Space: O(2^n * n), because memoization stores lists of generated sentences, plus O(n) recursion stack.