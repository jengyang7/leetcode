class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        # MOD = 10**9 + 7
        # ans = []

        # for l, r in (queries):
        #     num = 0
        #     digit_sum = 0
        #     for c in s[l:r+1]:
        #         if c != '0':
        #             d = int(c)
        #             num = (num * 10 + d) % MOD
        #             digit_sum += d
        #     ans.append((num * digit_sum) % MOD)
        
        # return ans

        # # time: O(M x Q) M: len of str, Q: number of queries
        # # space: O(Q) only store ans list

        MOD = 10**9 + 7
        n = len(s)

        # prefix_digit_sum[i] = sum of non-zero digits in s[0:i]
        prefix_digit_sum = [0] * (n + 1)

        # prefix_count[i] = number of non-zero digits in s[0:i]
        prefix_count = [0] * (n + 1)

        nonzero_digits = []

        for i, c in enumerate(s):
            digit = int(c)

            prefix_digit_sum[i + 1] = prefix_digit_sum[i] + digit
            prefix_count[i + 1] = prefix_count[i]

            if c != '0':
                prefix_count[i + 1] += 1
                nonzero_digits.append(digit)

        m = len(nonzero_digits)

        # pow10[i] = 10^i % MOD
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix_num[i] = number formed by nonzero_digits[0:i] modulo MOD
        prefix_num = [0] * (m + 1)
        for i in range(m):
            prefix_num[i + 1] = (prefix_num[i] * 10 + nonzero_digits[i]) % MOD

        ans = []

        for l, r in queries:
            digit_sum = prefix_digit_sum[r + 1] - prefix_digit_sum[l]

            left = prefix_count[l]
            right = prefix_count[r + 1]

            length = right - left

            # value of nonzero_digits[left:right]
            x = (prefix_num[right] - prefix_num[left] * pow10[length]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans