from typing import List

def read_integers() -> List[int]:
    userInput = input()
    return userInput.split(",")

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
