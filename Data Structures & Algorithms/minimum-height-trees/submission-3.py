class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Build an undirect graph by creating adjacent list
        adj_list = {i : [] for i in range(n)}
        for par, child in edges:
            adj_list[par].append(child)
            adj_list[child].append(par)
        
        # Define a bfs to calculat the height of the tree from each node
        def bfs(node: int, visited: set) -> int:
            # Mark current node as visited
            visited.add(node)
            queue = deque()
            queue.append(node)

            height = 0
            while queue:
                size = len(queue)
                for i in range(size):
                    # Get current node in this height
                    cur_node = queue.popleft()
                    for nei in adj_list[cur_node]:
                        if nei not in visited:
                            visited.add(nei)
                            queue.append(nei)
                height += 1
            return height

        res, mht = [], float("inf")    
        for i in range(n):
            cur_hei = bfs(i, set())
            print(cur_hei)
            if cur_hei < mht:
                mht = cur_hei
                res = [i]
            elif cur_hei == mht:
                res.append(i)
        return res
