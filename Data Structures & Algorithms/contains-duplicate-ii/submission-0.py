class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Define the size of the array nums
        n = len(nums)
        
        # Create left pointer to track the sliding window
        left = 0
        st = set()
        for i in range(n):
            # Remove element if the size of the window over the size limit (k + 1)
            if i - left > k:
                st.remove(nums[left])
                left += 1
            # If current num exist in the set
            if nums[i] in st:
                return True
            # Add current item to the set
            st.add(nums[i])

        return False