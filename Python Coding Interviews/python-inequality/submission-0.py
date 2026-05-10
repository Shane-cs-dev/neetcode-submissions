from typing import List


def is_arr_valid(names: List[str], max_length: int) -> bool:
    for name in names:
        if len(name) < 0 or len(name) > max_length:
            return False
    return True
            



# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 1))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 4))
