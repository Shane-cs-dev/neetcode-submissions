class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr: List[int], left: int, mid: int, right: int) -> None:
            # Define the sub array from arr 
            left_arr, right_arr = arr[left:mid + 1], arr[mid + 1:right + 1]

            # Define variables for both arrays and current index i
            i, j, k = left, 0, 0

            # Check the value in subarray and inplace update the array
            while j < len(left_arr) and k < len(right_arr):
                if left_arr[j] <= right_arr[k]:
                    arr[i] = left_arr[j]
                    j += 1
                else:
                    arr[i] = right_arr[k]
                    k += 1
                # Udpate current index
                i += 1

            while j < len(left_arr):
                arr[i] = left_arr[j]
                j += 1
                i += 1
            while k < len(right_arr):
                arr[i] = right_arr[k]
                k += 1
                i += 1
            return

        def mergeSort(arr: List[int], left: int, right: int) -> None:
            # Base case: Down to one num in arr
            if left >= right:
                return
            
            # Define the mid index
            mid = left + (right - left)//2

            # Calling for the sub list
            mergeSort(arr, left, mid)
            mergeSort(arr, mid + 1, right)

            # Merge the array once it return
            merge(arr, left, mid, right)

            
        mergeSort(nums, 0, len(nums) - 1)
        return nums


    def sortArray_heap(self, nums: List[int]) -> List[int]:
        # Using heap to sort the nums
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        
        return [heapq.heappop(heap) for i in range(len(nums))]