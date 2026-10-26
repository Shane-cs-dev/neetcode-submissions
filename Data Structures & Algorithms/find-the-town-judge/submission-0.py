class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        hash_map = defaultdict()
        # Loop through the array trust and update the hash map 
        for i in range(len(trust)):
            a, b = trust[i][0], trust[i][1]
            # Update the trust number
            if a not in hash_map:
                hash_map[a] = -1
            else:
                hash_map[a] -= 1
            if b not in hash_map:
                hash_map[b] = 1
            else:
                hash_map[b] += 1
            
        
        for key, value in hash_map.items():
            if value == n - 1:
                return key
        return -1
            