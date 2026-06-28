class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize the first string
        matched_str = strs[0]

        # Loop through the array strs
        for st in strs[1:]:
            # Corner case
            if not st:
                return ""
            # Calculate the min length for matching the common string
            len_str = min(len(st), len(matched_str))
            i = 0
            while i < len_str and st[i] == matched_str[i]:
                i += 1
            matched_str = matched_str[:i]
        
        return matched_str
                
