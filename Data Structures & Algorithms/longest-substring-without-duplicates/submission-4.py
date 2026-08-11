class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Create an empty set to track the sliding window
        st = set()

        # Loop through the string and check the longest string
        left = 0
        max_sub = 0
        for char in s:
            # If the char already in the set
            while char in st:
                st.remove(s[left])
                left += 1
            st.add(char)
            max_sub = max(max_sub, len(st))
        
        return max_sub