class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = defaultdict(int)

        # Count the number for the stirng s
        for ch in s:
            hashMap[ch] += 1
        
        # Check the number in t and return False if the count is < 0
        for ch in t:
            hashMap[ch] -= 1
            if hashMap[ch] < 0:
                return False

        # Final check
        for value in hashMap.values():
            if value > 0:
                return False
        
        return True
