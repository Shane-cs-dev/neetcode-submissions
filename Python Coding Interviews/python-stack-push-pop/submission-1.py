from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    # return arr[::-1]
    # Practice to use stack
    stack = []
    for num in arr:
        stack.append(num)
    new_arr = []
    while len(stack) > 0:
        new_arr.append(stack[-1])
        stack.pop()
    return new_arr


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
