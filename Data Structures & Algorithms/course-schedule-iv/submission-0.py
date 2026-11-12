class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create a direct graph adjacent list
        adj_list = {i : [] for i in range(numCourses)}
        for pre, cur in prerequisites:
            adj_list[pre].append(cur)
        
        # Define a dfs function to check whether the the user finish the prerequisites
        def dfs(node: int, target: int, visited: set) -> bool:
            # Base case:
            if node == target:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj_list[node]:
                if dfs(nei, target, visited):
                    return True
            return False
        
        ans = []
        for start, target in queries:
            if dfs(start, target, set()):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans