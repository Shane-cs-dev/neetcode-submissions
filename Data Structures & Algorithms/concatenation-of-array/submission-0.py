class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNum = nums
        for num in nums:
            newNum.append(num)
        return newNum