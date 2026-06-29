class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Define the frequency of the element and the value
        res = freq = 0
        for num in nums:
            if freq == 0:
                res = num
                freq += 1
            elif num == res:
                freq += 1
            else:
                freq -= 1
        
        return res