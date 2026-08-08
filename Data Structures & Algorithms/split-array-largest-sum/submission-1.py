class Solution:
    """
    This is binary search method
    """
    def splitArray(self, nums: List[int], k: int) -> int:
        # Define the left and right pointer
        left, right = max(nums), sum(nums)

        # Create a helper function to check if the minimize res is doable within k
        def helper(limit, k) -> bool:
            curr_sum = 0
            for num in nums:
                if curr_sum + num > limit:
                    k -= 1
                    if k <= 0:
                        return False
                    curr_sum = 0
                curr_sum += num
            return True

        # Binary search 
        while left < right:
            # Calculate mid
            mid = left + (right - left) // 2

            # If current sum is not valid
            if not helper(mid, k):
                left = mid + 1
            else:
                right = mid
        
        return left


























    """
    This is dfs method
    """
    def splitArray_dfs(self, nums: List[int], k: int) -> int:
        # Define the size of the array nums
        n = len(nums)
        

        # Define dp for memoization
        dp = [[-1] * (k + 1) for i in range(n)]

        # Define recursion function
        def helper(i, m) -> int:
            # Base case:
            # If the idx reach the end the of array 
            if i == n:
                return 0 if m == 0 else float('inf')
            # If there's no budge for the array
            if m == 0:
                return float('inf')
            
            # If we already calculated this one
            if dp[i][m] != -1:
                return dp[i][m]

            # If we haven't calculated this one
            res = float('inf')
            curr_sum = 0

            # Loop through the array from idx i and calculate the sum
            for j in range(i, n - m + 1):
                curr_sum += nums[j]

                # Check the sub_max
                sub_max = max(curr_sum, helper(j + 1, m - 1))

                # Update the res
                res = min(res, sub_max)
            
            # Record into the dp
            dp[i][m] = res
            return res
        
        return helper(0, k)