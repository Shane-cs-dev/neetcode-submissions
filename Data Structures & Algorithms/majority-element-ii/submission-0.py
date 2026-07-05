class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Define the size of the array nums
        n = len(nums)

        # Define varaibles for major two elements
        major1, major2 = 0, 0
        major_num1, major_num2 = -1, -1

        # loop through the array nums and calculate two major elements
        for num in nums:
            # Check if there's value for major_num1 and major_num2
            if major_num1 == -1:
                major_num1 = num
                major1 = 1
            elif major_num2 == -1:
                major_num2 = num
                major2 = 1
            # Check if curerent one is major element 1 or 2
            elif num == major_num1:
                major1 += 1
            elif num == major_num2:
                major2 += 1
            else:
                major1 -= 1
                major2 -= 1
        
        # Check if major number's count is more than n/3
        res = []
        major1 = major2 = 0
        for num in nums:
            if num == major_num1:
                major1 += 1
            elif num == major_num2:
                major2 += 1

        # Add the valided count into the res
        if major1 > n/3:
            res.append(major_num1)
        if major2 > n/3:
            res.append(major_num2)
        
        return res
