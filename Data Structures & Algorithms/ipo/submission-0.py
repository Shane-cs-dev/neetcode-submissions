class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create a tuple of (cur_capital, -cur_profit) so we can get the feasible captial with the best profit first  
        min_heap = [(c, -p) for p, c in zip(profits, capital)]  
        heapq.heapify(min_heap)

        # Corner case: if the original capital cannot do anything
        if min_heap and min_heap[0][0] > w:
            return 0
        
        # Create a max_heap to store the profits that previously pops
        max_heap = []
        while k:
            while min_heap and w >= min_heap[0][0]:
                heapq.heappush(max_heap, heapq.heappop(min_heap)[1])
            # Take the biggest one out of max_heap and update the w and k
            w += -heapq.heappop(max_heap)
            k -= 1
        return w
