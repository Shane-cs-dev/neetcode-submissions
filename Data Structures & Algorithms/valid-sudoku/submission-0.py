from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This equation can be used to verify the index of each square
        # (row/3) + (col/3)
        # Declare hashSet for rows, cols, and squares
        rows, cols, squares = defaultdict(set), defaultdict(set), defaultdict(set)

        # Check every location and update the hashSet
        for i in range(len(board)):
            for j in range(len(board[0])):
                # Define current number
                curr_num = board[i][j]
                if curr_num == ".":
                    continue
                # Define the key for squares
                r, c = i // 3, j // 3
                # Checking if the num is already existed in the hashSet
                if curr_num in rows[i] or curr_num in cols[j] or curr_num in squares[(r, c)]:
                    return False
                
                # Update the hashSet
                rows[i].add(curr_num)
                cols[j].add(curr_num)
                squares[(r, c)].add(curr_num)
        
        return True

        