class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # check each interval with other interval is it covered
        # compare left and right
        # ans = 0
        # n = len(intervals)

        # for i in range(n):
        #     for j in range(n):
        #         if i != j:
        #             if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
        #                 ans += 1
        
        # return n - ans

        # sort first
        intervals.sort(key=lambda x: (x[0], -x[1])) # sort first in asc and second in des
        count = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
        
        return count
        # time: O(nlogn)
        # space: O(1)