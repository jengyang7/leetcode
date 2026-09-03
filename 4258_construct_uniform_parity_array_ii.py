class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minimum = min(nums1)

        # if min is odd, always True because all numbers minus odd is odd
        if minimum % 2 == 1:
            return True
        
        # if min is even, and if there is 1 odd, then impossible
        for n in nums1:
            if n % 2 == 1:
                return False
        
        return True

        # time: O(n)
        # space: O(1)