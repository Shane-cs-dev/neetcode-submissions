class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Loop through the prerequisites and build an adjacent list
        adj_list = {i : [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            adj_list[pre].append(cur)
        
        # Define a function for dfs
        visited = set()
        def dfs(node: int) -> bool:
            # Base case:
            if node in visited:
                return False
            
            # if the node has no neighbor
            if adj_list == []:
                return True
            
            # Mark this path as visited
            visited.add(node)
            for nei in adj_list[node]:
                if not dfs(nei):
                    return False
            visited.discard(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True