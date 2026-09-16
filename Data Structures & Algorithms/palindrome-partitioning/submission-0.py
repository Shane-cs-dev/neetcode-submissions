class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res, temp = [], []

        # Define a function to check if the given string is palindrome
        def is_valid(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            
            return True
        
        # Define a function to find a all palidrome
        def dfs(idx: int) -> None:
            # Base case:
            if idx == len(s):
                self.res.append(temp[:])
                return
            
            # Loop through the string s
            for i in range(idx, len(s), 1): # Every size of the substring
                if is_valid(idx, i):
                    temp.append(s[idx:i + 1])
                    dfs(i + 1)
                    temp.pop()
            return
        
        dfs(0)
        return self.res
            