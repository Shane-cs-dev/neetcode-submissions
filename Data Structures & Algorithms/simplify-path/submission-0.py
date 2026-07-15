class Solution:
    def simplifyPath(self, path: str) -> str:
        # Define an empty array for stack
        stack = []
        # Separate the path by '/'
        paths = path.split('/')
        print(paths)

        for curr_str in paths:
            if curr_str == "..":
                if stack:
                    stack.pop()
            elif curr_str != "." and curr_str != "":
                stack.append(curr_str)
        return "/" + "/".join(stack)