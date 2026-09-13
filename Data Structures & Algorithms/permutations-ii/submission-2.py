from typing import List, Dict
from collections import defaultdict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Build the hash map for this array nums
        num_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        # Define a function for backtracking
        self.res = []
        def dfs(freq: Dict, temp: List) -> None:
            # Base case:
            if len(temp) == len(nums):
                self.res.append(temp[:])
                return
            
            # Loop through the dict freq and do backtracking
            for num, cnt in freq.items():
                if cnt > 0:
                    temp.append(num)
                    freq[num] -= 1
                    dfs(freq, temp)
                    freq[num] += 1
                    temp.pop()
            return
        
        dfs(num_freq, [])
        return self.res
        
