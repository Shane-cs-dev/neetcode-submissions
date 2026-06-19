class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        aSet = set()
        for num in nums:
            if (num in aSet):
                return True
            aSet.add(num)