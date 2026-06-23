class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        # Loop through the array sorted_num
        ans = []
        for num in nums:
            dict[num] += 1
            if (dict[num] >= k):
                if num not in ans:
                    ans.append(num)
        
        return ans

