class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate the length of the edge
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        tar_edge = total_len / 4

        # Sort the array 
        matchsticks.sort()
        print(matchsticks)
        # Create left and right pointer to count the numbe of valid edge
        left, right = 0, len(matchsticks) - 1
        count = 4
        while left <= right:
            # If one side is valid
            if matchsticks[left] == tar_edge:
                left += 1
                count -= 1
            elif matchsticks[right] == tar_edge:
                right -= 1
                count -= 1
            elif matchsticks[left] + matchsticks[right] == tar_edge:
                left += 1
                right -= 1
                count -= 1
            else:
                 return False

        return True