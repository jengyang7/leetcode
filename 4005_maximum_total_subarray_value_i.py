class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # find the global min and max
        # then k * (max-min)

        global_max = float("-inf")
        global_min = float("inf")

        for n in nums:
            global_max = max(global_max, n)
            global_min = min(global_min, n)
        
        return k * (global_max - global_min)

        # return k * (max(nums) - min(nums))