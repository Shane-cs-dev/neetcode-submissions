class MyHashSet:

    def __init__(self):
        self.st = set()

    def add(self, key: int) -> None:
        self.st.add(key)

    def remove(self, key: int) -> None:
        if key in self.st:
            self.st.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.st