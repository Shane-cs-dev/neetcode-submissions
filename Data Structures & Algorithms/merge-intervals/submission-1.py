class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        # Treat the first one as an newInterval and update the new array res
        res, newInterval = [], intervals[0]
        for i, (start, end) in enumerate(intervals[1:]):
            # No overlap, current one is at the right side of the newInterval
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i + 1:]
            else: # If ther's overlap
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]
            print(res)
        res.append(newInterval)
        return res
