class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a defaultdict and add the frequency of all char into it
        freq = defaultdict(int)
        freq['a'], freq['b'], freq['c'] = a, b, c
        print(freq)
        # Make it a min heap
        min_heap = [(-freq, char) for char, freq in freq.items() if freq > 0]
        heapq.heapify(min_heap)


        # Build a happy string
        res = ""
        while min_heap:
            cur_freq, cur_char = heapq.heappop(min_heap)
            # False condition:
            if len(res) > 1 and res[-1] == res[-2] == cur_char:
                # If there's no other char in the min_heap
                if not min_heap:
                    break
                # If there's other item in there
                next_freq, next_char = heapq.heappop(min_heap)
                res += next_char
                next_freq += 1
                # Add the item back to the heap if there's still char
                if next_freq:
                    heapq.heappush(min_heap, (next_freq, next_char))
            else:
                cur_freq += 1
                res += cur_char
            if cur_freq:
                heapq.heappush(min_heap, (cur_freq, cur_char))
        return res


