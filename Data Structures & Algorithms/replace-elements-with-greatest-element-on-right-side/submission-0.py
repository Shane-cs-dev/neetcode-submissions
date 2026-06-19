class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []

        prefix_num = -1
        for num in reversed(arr):
            ans.append(prefix_num)
            # update prefix_num
            prefix_num = max(prefix_num, num)

        return ans[::-1]