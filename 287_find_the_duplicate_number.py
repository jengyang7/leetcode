class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # find duplicate use hashmap with O(1) access and O(n) space
        # visited = set()

        # for n in nums:
        #     if n in visited:
        #         return n
        #     visited.add(n)

        # floyd cycle detection
        slow = 0
        fast = 0

        # find intersection
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        # find circle entrace = duplicate
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow
            

        # time: O(n)
        # space: O(1) - no need hashmap, just pointers