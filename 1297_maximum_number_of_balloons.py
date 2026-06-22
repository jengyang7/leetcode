class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        count = collections.defaultdict(int)

        # count the char frequency in text
        for c in text:
            if c in balloon_dict.keys():
                count[c] += 1

        res = float('inf')

        for char, required_freq in balloon_dict.items():
            possible_words = count[char] // required_freq
            res = min(res, possible_words)
        
        return res

        # time: O(n)
        # space: O(1) - 5 char