from typing import List, Dict
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Build a dict that tack the frequency of the num in nums
        freq = {num:0 for num in nums}
        for num in nums:
            freq[num] += 1
        temp = []

        # dfs function
        self.res = []
        def dfs() -> None:
            # Base case
            if len(temp) == len(nums):
                self.res.append(temp.copy())
                return
                    
            # Loop through the freq dict 
            for num, cnt in freq.items():
                if cnt > 0:
                    temp.append(num)
                    freq[num] -= 1
                    dfs()
                    temp.pop()
                    freq[num] += 1
            return
        
        dfs()
        return self.res