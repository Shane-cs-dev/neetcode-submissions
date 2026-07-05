from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Define hasp map and set value 1 for key 0
        dic = defaultdict(int)
        dic[0] = 1

        # Define variables for current sum and the count of the subarray equal to k
        curr_sum = 0
        count = 0

        for num in nums:
            # Update current sum
            curr_sum += num

            # Calculate the rest of the value 
            rest_val = curr_sum - k
            if rest_val in dic:
                count += dic[rest_val]
            
            # Update hasp map
            dic[curr_sum] += 1
        
        return count



