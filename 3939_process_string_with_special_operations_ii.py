class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lengths = [0] * n
        
        cur_len = 0

        for i, c in enumerate(s):
            if c.islower():
                cur_len += 1
            elif c == '*':
                cur_len = max(0, cur_len - 1)
            elif c == '#':
                cur_len *= 2
            # elif c == '%': # leave length unchanged
            lengths[i] = cur_len
        
        if k >= lengths[-1]: # out of bounds
            return '.'
               
        
        pos = k
        for i in range(n - 1, -1, -1): # operations
            ch = s[i]
            before_len = lengths[i - 1] if i > 0 else 0
            after_len = lengths[i]

            if ch.islower():
                if pos == before_len:
                    return ch
            elif ch == '*':
                pass # pos unchanged, before_len = after_len + 1
            elif ch == '#':
                pos = pos % before_len
            elif ch == '%':
                pos = after_len - 1 - pos
        
        return '.'

        # time: O(n)
        # space: O(n)