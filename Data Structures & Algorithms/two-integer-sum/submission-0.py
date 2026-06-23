class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an hash map and store the index
        hashMap = defaultdict()

        for i, num in enumerate(nums):
            rest = target - num
            if rest in hashMap:
                return [hashMap[rest], i]
            hashMap[num]=  i
        
        return []
