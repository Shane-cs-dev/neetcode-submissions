class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for start, end in intervals:
            # If we need to extend the newInterval
            if start <= newInterval[1] and end >= newInterval[0]:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
            else:
                res.append([start, end])
        
        res.append(newInterval)
        
        return sorted(res)