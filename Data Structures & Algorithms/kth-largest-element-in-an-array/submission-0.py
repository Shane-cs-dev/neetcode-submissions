class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a max heap and pop the heap maintain the size of the heap
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]