class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Corner case: s is longer than t
        if len(s) > len(t):
            return False
        
        
        # Sweep Line
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
