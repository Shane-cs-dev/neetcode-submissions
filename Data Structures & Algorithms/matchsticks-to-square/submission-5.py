class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate the length of the edge
        total_len = sum(matchsticks)

        if total_len % 4 != 0:
            return False
        tar_edge = total_len // 4
        
        # Sort the array in descending order
        matchsticks.sort(reverse = True)

        # Create an array of 4 edges for backtracking
        edges = [0] * 4

        # Define a dfe function to loop through the array and build the edges
        def dfs(idx: int) -> bool:
            # Base case:
            if idx == len(matchsticks):
                return True
            
            # Loop through the array edges
            for i in range(4):
                if edges[i] + matchsticks[idx] <= tar_edge:
                    edges[i] += matchsticks[idx]
                    if dfs(idx + 1):
                        return True
                    edges[i] -= matchsticks[idx]
                # The given edge is bigger than the target edge
                if edges[i] == 0:
                    break
            return False




        return dfs(0)