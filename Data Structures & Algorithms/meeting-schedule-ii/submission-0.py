"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Create two arrays sorted by start, and end respectively
        start_arr = sorted([interval.start for interval in intervals])
        end_arr = sorted([interval.end for interval in intervals])

        # Loop through the array of start and end
        s, e = 0, 0
        res, count = 0, 0
        while s < len(start_arr):
            # If there's no meeting ends
            if start_arr[s] < end_arr[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res