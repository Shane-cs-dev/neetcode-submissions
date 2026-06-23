class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for stri in strs:
            # Sort the string
            sorted_str = "".join(sorted(stri))
            res[sorted_str].append(stri)
        
        return list(res.values())
                

