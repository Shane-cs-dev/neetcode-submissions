class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Get the size of the mountainArr
        n = mountainArr.length()

        # Find the peak element inside of the mountainArr
        # Define left and right pointer
        left, right = 0, n - 1
        peak_idx = -1
        while left <= right:
            mid = left + (right - left) // 2

            # Attain the val of the left, mid, right index
            left_val, mid_val, right_val = mountainArr.get(left), mountainArr.get(mid), mountainArr.get(right)

            # current position at the left side of the peak
            if left_val < mid_val < right_val:
                left = mid + 1
            elif left_val > mid_val > right_val:
                right = mid - 1
            else:
                peak_idx = mid
                print(peak_idx)
                break
        
        # Search target in the left side of the array
        left, right = 0, peak_idx
        while left <= right:
            mid = left + (right - left) // 2

            left_val, mid_val, right_val = mountainArr.get(left), mountainArr.get(mid), mountainArr.get(right)

            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"This is left side: {left}")
        # Search target in the right side of the array
        left, right = peak_idx + 1, n - 1
        while left <= right:
            mid = left + (right - left) // 2

            left_val, mid_val, right_val = mountainArr.get(left), mountainArr.get(mid), mountainArr.get(right)

            if mid_val == target:
                return mid
            elif mid_val > target:
                left = mid + 1
            else:
                right = mid - 1
        print(f"This is right side: {left}")
        return -1
            