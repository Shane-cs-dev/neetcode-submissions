class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Define the size of the row and col
        r, c = len(matrix), len(matrix[0])

        def binary_search(x) -> int:
            left, right = 0, x

            while left < right:
                mid = left + (right - left + 1) // 2

                if matrix[mid][0] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
        
        def binary_search2(x, r) -> int:
            left, right = 0, x

            while left < right:
                mid = left + (right - left + 1) // 2

                if matrix[r][mid] <= target:
                    left = mid
                else:
                    right = mid - 1
            return left
        
        row = binary_search(r)
        col = binary_search2(c, row)
        result = True if matrix[row][col] == target else False

        return result