from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        # Check the frequency
        counter = Counter(s)

        # Create a list of [cnt, char]
        min_heap = [(-frequency, char) for char, frequency in counter.items()]
        heapq.heapify(min_heap)

        # Create an prev to deal with continuous char and res for the answer
        prev, res = None, ""

        while prev or min_heap:
            if prev:
                if not min_heap:
                    if prev[0] < 0:
                        return ""
                    break
                else: # If we have the next one
                    next_cnt, next_char = heapq.heappop(min_heap)
                    next_cnt += 1
                    res += next_char
                    # Udpate prev
                    prev_cnt, prev_char = prev
                    if prev_cnt < 0:
                        heapq.heappush(min_heap, prev)
                    prev = (next_cnt, next_char)
            else:
                if min_heap:
                    next_cnt, next_char = heapq.heappop(min_heap)
                    res += next_char
                    next_cnt += 1
                    # Update prev
                    prev = (next_cnt, next_char)
        return res