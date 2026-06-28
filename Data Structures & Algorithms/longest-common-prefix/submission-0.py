class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize the first string
        matched_string = strs[0]

        # Loop through the array strs
        for st in strs[1:]:
            # Calculate the min length for matching the common string
            len_str = min(len(st), len(matched_string))
            for i in range(len_str):
                if st[i] != matched_string[i]:
                    matched_string = matched_string[:i]
                    break
        
        return matched_string
                
