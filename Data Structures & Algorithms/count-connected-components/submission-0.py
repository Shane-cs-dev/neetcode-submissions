class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create an adjcent list
        adj_list = {i : [] for i in range(n)}
        for pre, cur in edges:
            adj_list[pre].append(cur)
            adj_list[cur].append(pre)
        
        # Define a dfs function to traverse all connected node
        visited = set()
        def dfs(node: int) -> None:
            # Base case:
            if node in visited:
                return
            
            # Mark this node as visited
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)
            return
        
        components = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                components += 1
        
        return components
