class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Define the number of the node
        n = len(edges)

        # Create an adjacent list for this undirect graph
        adj_list = {i : [] for i in range(1, n + 1, 1)}
        for pre, cur in edges:
            adj_list[pre].append(cur)
            adj_list[cur].append(pre)
        
        # define a function to traverse the graph
        visited, cycle = set(), set()
        cycle_start = -1
        def dfs(node: int, par: int) -> bool:
            nonlocal cycle_start
            # Base case: Once we detect a cycle
            if node in visited:
                cycle_start = node
                return True
            
            # Mark this location as visited
            visited.add(node)
            for nei in adj_list[node]:
                if nei != par:
                    if dfs(nei, node):
                        if cycle_start != -1:
                            cycle.add(node)
                        if cycle_start == node:
                            cycle_start = -1
                        return True
            return False
        
        # Calling dfs to update the cycle 
        dfs(1, -1)

        for pre, cur in edges[::-1]:
            if pre in cycle and cur in cycle:
                return [pre, cur]
        return []

