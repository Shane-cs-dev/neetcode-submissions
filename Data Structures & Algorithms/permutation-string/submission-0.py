class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Define the size of the sliding window
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        # Create an array of size 26 to represent all lowercase letter
        freq = [0] * 26

        for char in s1:
            freq[ord(char) - ord('a')] += 1
        
        # Sliding window
        left = 0
        match_cnt = n
        for i in range(len(s2)):
            # Add current update current value into the window
            curr_ch = s2[i]
            freq[ord(curr_ch) - ord('a')] -= 1
            if freq[ord(curr_ch) - ord('a')] >= 0:
                match_cnt -= 1
            
            # Update left pointer to maintain the size of the sliding window
            if i >= n:
                left_ch = s2[left]
                if freq[ord(left_ch) - ord('a')] >= 0:
                    match_cnt += 1
                freq[ord(left_ch) - ord('a')] += 1
                left += 1
            
            # Check the valid window
            if match_cnt == 0:
                return True
                
        return False