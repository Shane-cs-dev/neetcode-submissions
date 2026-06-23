class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = defaultdict(int)

        # Loop through the array nums
        for num in nums:
            dict[num] += 1

        # Group the num by frequency
        arr = []
        for num, freq in dict.items():
            arr.append([freq, num])

        # Sort the array based on the freq
        arr.sort(reverse = True)

        ans = []
        for i in range(k):
            ans.append(arr[i][1])
        
        return ans

