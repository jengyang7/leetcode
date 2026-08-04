class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]
        
        # Convert to a set for instant O(1) lookups
        num_set = set(nums)
        res = []

        for i in range(min_val, max_val):
            if i not in num_set:
                res.append(i)
        
        # res is already built in sorted order!
        return res