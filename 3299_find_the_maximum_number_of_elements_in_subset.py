class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        elm_count = collections.Counter(nums)
        ans = 0

        # special case for 1
        if elm_count[1] > 0:
            if elm_count[1] % 2 == 1: # odd
                ans = elm_count[1] 
            else:
                ans = elm_count[1] - 1
        
        # try every num as start
        for start in nums:
            if start == 1:
                continue # ady handle
            
            x = start
            length = 0

            while elm_count[x] >= 2:
                length += 2
                x = x * x
            
            # need one middle
            if elm_count[x] >= 1:
                length += 1
            else:
                length -= 1 # no middle, remove one from previous pair
            
            ans = max(ans, length)

        return ans
            
        # time: O(log log M) where M is max of nums
        # space: O(n) for count for each element