class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Create an indegree array for all courses and build an adjacent list
        indegree = [0] * numCourses
        adj_list = {i : [] for i in range(numCourses)}
        for cur, pre in prerequisites:
            adj_list[pre].append(cur)
            indegree[cur] += 1
        

        # Create a queue and initialize by adding node with indegree 0
        queue = deque(i for i in range(len(indegree)) if indegree[i] == 0)

        # Khan's Algorithm
        courses = []
        while queue:
            # Get the course with 0 indegree
            cur_course = queue.popleft()
            courses.append(cur_course)

            for nei in adj_list[cur_course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return courses