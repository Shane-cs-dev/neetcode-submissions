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
            len_of_string = int(s[i])
            i += 2
            res.append(s[i: (i + len_of_string)])

            # update index for the next round
            i += len_of_string
        
        return res
