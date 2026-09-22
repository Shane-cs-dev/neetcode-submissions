class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Invert the list by given minus
        new_stones = [-stone for stone in stones]

        # Create a max_heap
        heapq.heapify(new_stones)
        print(new_stones)

        while len(new_stones) > 1:
            # Define fisrt and second stone
            first_s = -heapq.heappop(new_stones)
            sec_s = -heapq.heappop(new_stones)

            if first_s == sec_s:
                continue
            else:
                print(f"First stone: {first_s}, Second stone: {sec_s}")
                heapq.heappush(new_stones, -abs(first_s - sec_s))
        
        return 0 if len(new_stones) == 0 else -new_stones[0]
