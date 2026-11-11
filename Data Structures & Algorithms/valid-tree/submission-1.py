class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create an adjacent list for the undirect graph
        adj_list = {i : [] for i in range(n)}
        for pre, cur in edges:
            adj_list[pre].append(cur)
            adj_list[cur].append(pre)
        
        # Define a dfs function for cycle detection
        visited = set()
        def dfs(node: int, parent: int) -> bool:
            # Base case:
            if node in visited:
                return False
            
            # Mark as visited
            visited.add(node)
            for nei in adj_list[node]:
                if nei != parent:
                    if not dfs(nei, node):
                        return False
            return True
        
        return dfs(0, -1) and len(visited) == n