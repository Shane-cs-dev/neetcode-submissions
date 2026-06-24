class Solution:

    def encode(self, strs: List[str]) -> str:
        new_string = ""
        for st in strs:
            new_string += str(len(st)) + '#' + st

        return new_string

    def decode(self, s: str) -> List[str]:
        res = []
        # define the index for encode string
        i = 0

        while i < len(s):
            j = i
            # Skip anything that is not #
            while s[j] != '#':
                j += 1
            
            # This should be the #
            len_of_string = int(s[i:j])

            # Append current string into the res
            res.append(s[j + 1 : j + 1 + len_of_string])

            # update the index i
            i = j + 1 + len_of_string 

        return res
