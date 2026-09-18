from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Corner case:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Define a dfs to do backtracking
        self.res = []
        def dfs(temp: str, idx: int) -> None:
            # Base case:
            if len(temp) == len(digits):
                self.res.append(temp)
                return
            
            for i in range(idx, len(digits), 1):
                # Define the digit
                digit = digits[idx]
                for char in digitToChar[digit]:
                    dfs(temp + char, i + 1)
            return
        
        dfs("", 0)
        return self.res