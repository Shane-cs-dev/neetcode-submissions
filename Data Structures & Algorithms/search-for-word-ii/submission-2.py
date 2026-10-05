class TrieNode:
    def __init__(self):
        self.children = {}
        self.cur_str = ""

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add_word(self, word: str):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.cur_str = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Loop through the list of words and add word into the Trie
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        # Loop through the board and check every cells via dfs
        self.ans = []
        def dfs(r: int, c: int, node: TrieNode) -> None:
            # Base case: Out of bound, invalid cell (re-visit)
            if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
                return
            if board[r][c] == '&':
                return
            
            # If the char does not match any of the children in this node
            if board[r][c] not in node.children:
                return
            
            # If the char exists in current node's children
            node = node.children[board[r][c]]
            if node.cur_str != "":
                self.ans.append(node.cur_str)
                node.cur_str = ""
            # Mark the location as visit / Backtracking
            temp = board[r][c]
            board[r][c] = '&'

            dfs(r + 1, c, node)
            dfs(r, c + 1, node)
            dfs(r - 1, c, node)
            dfs(r, c - 1, node)
            board[r][c] = temp

            return
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.root)
        
        return self.ans

























