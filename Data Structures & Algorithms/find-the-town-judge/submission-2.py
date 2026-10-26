class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Define a hash map to track the trust
        hash_map = defaultdict(int)

        # Loop through the array trust
        for a, b in trust:
            if a in hash_map:
                hash_map.pop(a, None)
            hash_map[b] += 1
        
        # Check if there's Town Judge
        for key, val in hash_map.items():
            if val == n - 1:
                return key
        return -1

            