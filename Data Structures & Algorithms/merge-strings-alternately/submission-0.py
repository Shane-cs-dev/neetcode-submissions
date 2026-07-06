class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Define sweep line for two words
        p1, p2 = 0, 0

        res = ""
        while p1 < len(word1) and p2 < len(word2):
            res += word1[p1]
            res += word2[p2]
            p1 += 1
            p2 += 1
        
        print(res)
        # Check the index for pointers
        if p1 < len(word1):
            res += word1[p1:]
        elif p2 < len(word2):
            res += word2[p2:]
        
        return res