class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Using heap to sort the nums
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        
        return [heapq.heappop(heap) for i in range(len(nums))]