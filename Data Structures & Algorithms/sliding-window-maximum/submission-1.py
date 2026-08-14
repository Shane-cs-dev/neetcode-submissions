from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Storing the index
        left = 0
        res = []
        for i in range(len(nums)):
            while q and q[0] < nums[i]:
                q.popleft()
            q.append(i)

            # Check if the left most index is still valid
            if left > q[0]:
                q.popleft()
            
            # Start from the valid window size
            if i >= k - 1:
                res.append(nums[q[0]])
        
        return res

            

