class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # define index for s and t
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        print(i)
        print(j)


        return len(t) - j