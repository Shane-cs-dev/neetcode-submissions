class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        for ch in s:
            hashMap[ch] += 1
        
        for ch in t:
            hashMap[ch] -= 1
            if hashMap[ch] < 0:
                return False
        # Final check
        if len(s) != len(t):
            return False
        return True
