class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        altitude = 0

        for n in gain:
            altitude = altitude + n
            res = max(res, altitude)

        return res

        # time: O(n)
        # space: O(1)