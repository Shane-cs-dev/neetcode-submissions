class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Corner case:
        if endWord not in wordList:
            return 0

        # Build an adjacent list
        wordList.append(beginWord)
        neighbor = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbor[pattern].append(word)
        
        # Verify the result
        for pattern, nei in neighbor.items():
            print(f"{pattern}: {nei}")
        

        queue = deque([beginWord])
        visited = set()
        visited.add(beginWord)

        steps = 1
        while queue:
            # Calculate the number of current layer
            number = len(queue)
            for i in range(number):
                # Get the current word and loop through every char
                cur_word = queue.popleft()
                for j in range(len(cur_word)):
                    pattern = cur_word[:j] + '*' + cur_word[j + 1:]
                    for nei in neighbor[pattern]:
                        if nei == endWord:
                            return steps + 1       
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
            steps += 1
        
        return 0