class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Corner case: s is longer than t
        if len(s) > len(t):
            return False
        
        hashMap = defaultdict(int)

        for ch in t:
            hashMap[ch] += 1
        
        # Calculate the count of the ch and return false if the count is less than 0
        for ch in s:
            hashMap[ch] -= 1
            if (hashMap[ch] < 0):
                return False
        
        return True