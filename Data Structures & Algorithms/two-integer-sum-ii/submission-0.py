class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Define the size of the array numbers
        n = len(numbers)

        # Return the index
        def binary_search(left: int, target: int) -> int:
            right = n - 1
            # Binary search 
            while left <= right:
                # Define the mid index
                mid = left + (right - left)//2

                # Check the value
                if numbers[mid] == target:
                    return mid
                elif numbers[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Loop through the array numbers
        for i in range(n):
            # Define the rest of the value from target
            rest = target - numbers[i]

            # Calling helper function to check the valid index
            j = binary_search(i + 1, rest)
            if j != -1:
                return [i + 1, j + 1]
            
        return []