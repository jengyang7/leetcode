class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Add the baseline boundary for the first building [id, max_height]
        restrictions.append([1, 0])
        
        # Sort restrictions by building ID from left to right
        restrictions.sort()
        
        # Add a theoretical maximum restriction for the last building to handle edge cases
        if restrictions[-1][0] != n:
            restrictions.append([n, n - 1])
            
        m = len(restrictions)
        
        # 2. Left-to-Right Pass: Propagate restrictions forward
        # A building's height cannot exceed the previous building's height + distance
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)
            
        # 3. Right-to-Left Pass: Propagate restrictions backward
        # A building's height cannot exceed the next building's height + distance
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)
            
        # 4. Calculate the global maximum height peak between every adjacent pair
        max_height = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            dist = id2 - id1
            
            # Math formula to find the absolute maximum peak between two restricted bounds:
            # peak = (distance + height1 + height2) // 2
            current_max = (dist + h1 + h2) // 2
            max_height = max(max_height, current_max)
            
        return max_height

        # time: O(mlogn)
        # space: O(mlogn)