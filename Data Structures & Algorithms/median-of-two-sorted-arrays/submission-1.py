class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A
        
        # Define left and right pointer
        left, right = 0, len(A) - 1

        while True:
            # Calculate mid value
            mid = left + (right - left) // 2 # A
            j = half - mid - 2 # B, 2 is the index 0 from both array

            # Define value at the left and right 
            Aleft = A[mid] if mid >= 0 else float('-inf')
            Aright = A[mid + 1] if mid + 1 < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            # If the left partition is correct
            if Bright >= Aleft and Aright >= Bleft:
                # If the total len of two arrays are even
                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                # If the total length of the merged array is odd
                else:
                    return min(Aright, Bright)
            else:
                if Bright < Aleft:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


