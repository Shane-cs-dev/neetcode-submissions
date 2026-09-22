class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Invert the list by given minus
        new_stones = [-stone for stone in stones]

        # Create a max_heap
        heapq.heapify(new_stones)

        while len(new_stones) > 1:
            # Define fisrt and second stone
            first_s, sec_s = -new_stones[0], -new_stones[1]
            heapq.heappop(new_stones)
            heapq.heappop(new_stones)

            if first_s == sec_s:
                continue
            else:
                print(f"First stone: {first_s}, Second stone: {sec_s}")
                heapq.heappush(new_stones, -abs(first_s - sec_s))
        
        return -new_stones[0]
