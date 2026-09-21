class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
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