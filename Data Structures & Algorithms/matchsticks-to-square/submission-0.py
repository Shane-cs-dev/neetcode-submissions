class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate the length of the edge
        total_len = sum(matchsticks)
        if total_len % 4 != 0:
            return False
        tar_edge = total_len / 4

        


        return True