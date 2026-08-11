class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create an empty set to track the sliding window
        st = set()

        # Loop through the string and check the longest string
        left = 0
        max_sub = -1
        for char in s:
            # If the char already in the set
            if char in st:
                max_sub = max(max_sub, len(st))
                st.remove(s[left])
                left += 1
            st.add(char)
        
        return max(max_sub, len(st))