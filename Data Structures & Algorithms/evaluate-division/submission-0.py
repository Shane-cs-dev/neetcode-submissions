class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Create a dictionary for the adjacent list storing the neighbor and the value accordingly
        adj_list = defaultdict(list)
        for i in range(len(equations)):
            pre, cur = equations[i]
            adj_list[pre].append((cur, values[i]))
            adj_list[cur].append((pre, 1.0/values[i]))
        
        # Define a function to traverse the node and calcualte the value
        def dfs(src: str, des: str, visited: set) -> int:
            # Base case:
            if src not in adj_list or des not in adj_list:
                return -1
            if src == des:
                return 1
            
            # Mark this location as visited
            visited.add(src)

            for nei, weight in adj_list[src]:
                if nei not in visited:
                    result = dfs(nei, des, visited)
                    if result != -1:
                        return result * weight
            return -1
        
        return [dfs(pre, cur, set()) for pre, cur in queries]