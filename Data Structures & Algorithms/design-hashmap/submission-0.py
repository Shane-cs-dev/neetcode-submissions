class MyHashMap:

    def __init__(self):
        self.sim_hash = []

    def put(self, key: int, value: int) -> None:
        for item in self.sim_hash:
            # If there's a key in the sim_hash, update the value
            if key == item[0]:
                item[1] = value
                return 
        # if there's no key found in the sim_hash
        self.sim_hash.append([key, value])

    def get(self, key: int) -> int:
        for item in self.sim_hash:
            # return value if the key matches
            if key == item[0]:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        for i, item in enumerate(self.sim_hash):
            if item[0] == key:
                self.sim_hash.pop(i)
                return