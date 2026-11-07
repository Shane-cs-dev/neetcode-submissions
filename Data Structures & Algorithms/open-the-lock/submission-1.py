class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Put the list of deadends to the set
        visited = set(deadends)

        if target in deadends:
            return -1

        # Define a function to tune each digit to its neghbor for either adding one or minus one
        def neighbor(val_str: str) -> Optional[List]:
            nei = []
            for i in range(len(target)): #loop through each digit
                digit = (int(val_str[i]) + 1) % 10
                nei.append(val_str[:i] + str(digit) + val_str[i + 1:])
                digit = (int(val_str[i]) + 10 - 1) % 10
                nei.append(val_str[:i] + str(digit) + val_str[i + 1:])
            return nei
        
        # Create a queue and store the current res and turn into it
        queue = deque()
        queue.append(("0000", 0))
        
        while queue:
            cur_nei, turns = queue.popleft()
            for nei in neighbor(cur_nei):
                if nei == target:
                    return turns + 1
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, turns + 1))
    
        return -1



            
