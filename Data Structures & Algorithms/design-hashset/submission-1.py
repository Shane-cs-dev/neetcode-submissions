class MyHashSet:

    def __init__(self):
        self.st = []

    def add(self, key: int) -> None:
        if key not in self.st:
            self.st.append(key)

    def remove(self, key: int) -> None:
        if key in self.st:
            self.st.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.st