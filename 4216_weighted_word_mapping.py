class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""

        if not words:
            return ''
        
        for word in words:
            word_sum = 0
            for c in word:
                word_sum += weights[ord(c) - ord('a')]
            remainder = word_sum % 26
            mapped_char = chr(ord('z') - remainder)
            res += mapped_char
        
        return res

        # time = O(n x l) number of word and char in each word
        # space = O(1)