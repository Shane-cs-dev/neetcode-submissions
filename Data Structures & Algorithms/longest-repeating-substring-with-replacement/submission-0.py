class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Create an empty Hashmap
        mp = {}

        # Loop through the string
        left = 0
        max_freq = 0
        max_sub = 0
        for i in range(len(s)):
            # Update the freq in hashmap
            mp[s[i]] = mp.get(s[i], 0) + 1
            max_freq = max(max_freq, mp[s[i]])

            # If the length of the sliding window - the maximum of the freq <= k: Valid window
            while (i - left + 1) - max(mp.values()) > k:
                mp[s[left]] -= 1
                left += 1
            
            max_sub = max(max_sub, i - left + 1)

        return max_sub