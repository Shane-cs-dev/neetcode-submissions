from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        cache = {}

        # Define a method to do backtracking
        def backtrack(idx: int) -> List:
            # Base case:
            if idx == len(s):
                return [""]
            if idx in cache:
                return cache[idx]

            # if this is a new location
            ans = []
            for i in range(idx, len(s), 1):
                # Define the sub-string
                sub_string = s[idx: i + 1]
                if sub_string not in wordSet:
                    continue
                
                # If the sub_stirng is valid
                strings = backtrack(i + 1)

                # Loop through the valid string
                for string in strings:
                    sentence = sub_string
                    if string:
                        sentence += " " + string
                    ans.append(sentence)
                
            cache[idx] = ans
            return ans
        
        return backtrack(0)


















    def wordBreak_1(self, s: str, wordDict: List[str]) -> List[str]:
        # Create a result list to store valid sentences
        self.res = []
        temp = []

        # Define a function to find valid sentence
        def backtrack(idx: int) -> None:
            # Base case:
            if idx == len(s):
                copy = " ".join(temp)
                self.res.append(copy)
                return
            
            # Check if there's a valid word
            for word in wordDict:
                if s.startswith(word, idx):
                    temp.append(word)
                    backtrack(idx + len(word))
                    temp.pop()
            return
        
        backtrack(0)
        return self.res