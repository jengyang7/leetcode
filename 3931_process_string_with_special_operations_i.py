class Solution:
    def processStr(self, s: str) -> str:
        if not s:
            return ""

        res = ""

        for c in s:
            if c == '*':
                res = res[:-1]
            elif c == '#':
                res = res + res
            elif c == '%':
                # tmp = res
                res = res[::-1]
                # res = ''
                # for j in range(len(tmp) - 1, -1, -1):
                #     res += tmp[j]
            elif 'a' <= c <= 'z':
                res += c
            print(res)
        return res

        # time: O(n2) - duplicating and reversing take O(n) too
        # time: O(1)