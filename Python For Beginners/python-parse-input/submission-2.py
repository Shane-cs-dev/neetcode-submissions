from typing import List

def read_integers() -> List[int]:
    userInput = input()
    list = userInput.split(",")
    for idx in range(len(list)):
        list[idx] = int(list[idx])
    return list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
