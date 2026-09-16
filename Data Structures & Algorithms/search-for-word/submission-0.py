class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Define a function to find the word in the board
        def dfs(r: int, c: int, idx: int) -> bool:
            # Base case:
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] == '#':
                return False
            if word[idx] != board[r][c]:
                return False
            if idx == len(word) - 1:
                return True
            
            # This char in the word match the char in the board[r][c]
            temp = board[r][c]
            # Udpate the board to mark as visited
            board[r][c] = '#'
            res = dfs(r + 1, c, idx + 1) or dfs(r, c + 1, idx + 1) or dfs(r - 1, c, idx + 1) or dfs(r, c - 1, idx + 1)
            board[r][c] = temp

            return res
        
        # Loop through the board and check the word if the first char matches
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] == word[0]):
                    if dfs(i, j, 0):
                        return True
        
        return False