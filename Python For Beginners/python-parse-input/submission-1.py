from typing import List

def read_integers() -> List[int]:
    userInput = input()
    list = userInput.split(",")
    for num in list:
        int(num)
    return list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
