class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # convert to string, remove the 0, then convert back to int to sum up
        n_str = str(n)
        p_str = '' # positive string
        sum = 0

        for c in n_str:
            if c != '0':
                p_str += c
                sum += int(c)
        
        if p_str == '':
            return 0
        
        return int(p_str) * sum