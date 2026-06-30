class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0
        n = len(s)

        for right in range(n):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right
                count[s[left]] -= 1
                left += 1
        
        return ans

        # time: O(n) for iterate n and left move n O(n+n) = O(n)
        # space: O(1) only store 3 count