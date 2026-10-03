class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        # Define a dfs function to check if the remaining word is valid
        def dfs(idx: int, node: TrieNode) -> bool:
            # Base case:
            if idx == len(word):
                return node.end_of_word
            
            # if the char is '.'
            if word[idx] == '.':
                for key, child in node.children.items():
                    if dfs(idx + 1, child):
                        return True
            else:
                if word[idx] not in node.children:
                    return False
                else:
                    return dfs(idx + 1, node.children[word[idx]])
            
        return dfs(0, self.root)