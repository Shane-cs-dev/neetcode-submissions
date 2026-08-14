from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        # Calculate the frequency of t
        for char in t:
            freq[char] += 1
        
        # Sliding window
        left = 0
        count = len(t)
        min_sub = float('inf')
        res = ""
        for i in range(len(s)):
            # Add current char into the window
            freq[s[i]] -= 1
            if freq[s[i]] >= 0:
                count -= 1

            # Shrink the window
            while i - left + 1 > len(t) and count != 0:
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count += 1
                left += 1
            

            if count == 0:
                if i - left + 1 < min_sub:
                    min_sub = i - left + 1
                    res = s[left:i + 1] 
        
        return res

