class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort the array intervals in ascending order
        intervals.sort()
        # print(intervals)
        
        # Loop through every intervals and update the last end value for another round of comparison
        res, last_end = 0, intervals[0][1]
        for i, (start, end) in enumerate(intervals[1:]):
            if start < last_end:
                # print(f"{start}: vs last_end: {last_end}")
                res += 1
                last_end = min(last_end, end)
            else:
                last_end = end
        return res