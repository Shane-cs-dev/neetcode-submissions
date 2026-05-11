from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    ans = []
    for lists in nested_arr:
        temp = float('-inf')
        for intr in lists:
            temp = max(intr, temp)
        ans.append(temp)
    return ans


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
