class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Create an array to track the trust number
        arr = [0] * (n + 1)

        # Loop through the trust array and update the arr
        for a, b in trust:
            arr[a] -= 1
            arr[b] += 1
        
        # Check if there's Town Judge
        for i in range(1, len(arr)):
            if arr[i] == n - 1:
                return i
        return -1